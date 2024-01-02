# Last changed on 27/12/2023
# Last changed is 409 -435 disabled condition 5 disabled
# last changed on 28/12/2023 disabled condition 4
# last changed on 02/01/2024 added new field to Project resp to CPROLEAD

import json
from datetime import datetime
import re

# 760 methods to create 760 records to delete from concor
def for_760(empid,bamboo_input,emp_id,bamboo_name_id,bamboo_ID,date_for_bamboo,converted_input):
                                    
    bamboo_list=bamboo_input
    Bamboo_ID=None
    Employee_ID=None
    Employee_Text=None
    employee_termination_date=None
    matched_760=False
    try:
        #for each list of bamboo list
        for items in bamboo_list:
            # CZ8A3365DF41600F8C
            #if bomboo emp id matching with emp_id
            if items.get(emp_id)==empid or items.get(bamboo_name_id)== empid:
                Bamboo_ID=items.get(bamboo_ID)      
                Employee_ID=items.get(emp_id)
                Employee_Text=items.get(bamboo_name_id)  
                employee_termination_date=items.get(date_for_bamboo)
                break
                
                #condition to check Bamboo_ID is None
            
        if (Bamboo_ID != None and empid != None ):
            prev_employee=Bamboo_ID
        else:
            prev_employee=empid
        

        if (prev_employee != None and len(prev_employee)> 0 ):
            #check cpondition for project not closed and employee not terminated
            if (converted_input.get("TPROPRSTLC")!= "Closed") and ("9999" in employee_termination_date):
                matched_760=True
                Approvers_List={
                    "column1":"760",
                    "column2":"PMT",
                    "column3":prev_employee,
                    "column4":converted_input.get("CCOMPANY"),
                    "column5":converted_input.get("CPROFITCTR"),
                    "column6":converted_input.get("CPROJECT"),
                    "column7":None,
                    "column8":None,
                    "column9":None,
                    "column10":None,
                    "column11":None,
                    "column12":None,  
                        }   
                return {"Approvers_List":Approvers_List,"matched_760":matched_760}
            else:
                return{"no_data":True,"matched_760":matched_760}
        else:
                return{"no_data":True,"matched_760":matched_760}        # Approvers_List1_array.append(Approvers_List)
        # else:
        #     if converted_input.get("TPROPRSTLC")!= "Closed":
        #         failed_condition_count.append(sap_items)
                # failed_co.append(f"{prev_employee}-{empid}-{Employee_ID}-{Previous_Lead}-{proj_lead}-{PRF}-{Project_Lead}")
                return {"Approvers_List":Approvers_List}


    except Exception as e:
        return {"error":f"${e} while creating empid"}
    

# 710 methods to create 760 records to add to concor    
def for_710(empid2,bamboo_input,emp_id,bamboo_name_id,bamboo_ID,date_for_bamboo,converted_input):
    Bamboo_ID=None
    Employee_ID=None
    Employee_Text=None
    employee_termination_date=None
    bamboo_list=bamboo_input
    try:
        #for each of bamboo_list for check employee id 
        for items in bamboo_list:
            if items.get(emp_id)==empid2 or items.get(bamboo_name_id)== empid2:
                Bamboo_ID=items.get(bamboo_ID)
                if Bamboo_ID==None or len(Bamboo_ID)==0:
                    Bamboo_ID=converted_input.get("CPROLEAD")
                Employee_ID=items.get(emp_id)
                Employee_Text=items.get(bamboo_name_id)
                employee_termination_date=items.get(date_for_bamboo)
                break
            else:
                # if employee Id is null
                if (empid2==None or len(empid2)==0):
                    empid2=converted_input.get("CPROLEAD")
                    if items.get(emp_id)==empid2:
                        Bamboo_ID=items.get(bamboo_ID)
                        employee_termination_date=items.get(date_for_bamboo)
                        if Bamboo_ID==None or len(Bamboo_ID)==0:
                            Bamboo_ID=converted_input.get("CPROLEAD")   
                            # Employee_ID=items.get(emp_id)
                        # Bamboo_ID=Employee_ID
                        # Employee_Text=items.get("TZ8A3365DF41600F8C") 
                        break
    # -------------------------
        if (Bamboo_ID !=None):
            employee=Bamboo_ID
        else:
            # employee=empid2             CPRORESPEM
            employee=converted_input.get("CPROLEAD") 
        #for employee who are not having bamboo record
        if (employee_termination_date==None):
            employee_termination_date="9999-12-30"
            employee=converted_input.get("CPROLEAD")
         #check cpondition for project not closed and employee not terminated
        if (converted_input.get("TPROPRSTLC")!="Closed") and ("9999" in employee_termination_date):
            Approvers_List2={
                        "column1":"710,PMT",
                        "column2":employee,
                        "column3":converted_input.get("CCOMPANY"),
                        "column4":converted_input.get("CPROFITCTR"),
                        "column5":converted_input.get("CPROJECT"),
                        "column6":None,
                        "column7":None,
                        "column8":None,
                        "column9":None,
                        "column10":None,
                        "column11":None,
                        "column12":None ,
                        "column13":None,
                        "column14":None,
                        "column15":1000000,
                        "column16":"USD"
                    }
            return {"Approvers_List":Approvers_List2}
        else:
            return{"no_data":True}   
         
    except Exception as e:
        return {"error":f"${e} while creating Approvers_List2"}
    
def main(input):
    #input from workato
    sap_input = input["sap_input"]
    bamboo_input=input["bamboo_item"]
    Approvers_List1_array=[]
    called_count_760=0
    called_count_710=0
    matched_760=0
    # Approvers_List2_array=[]
    error_list=[]
    CCOMPANY=input["CCOMPANY"]
    CPROFITCTR=input["CPROFITCTR"]
    CPROJECT=input["CPROJECT"]
    CPROPRSTLC=input["CPROPRSTLC"]
    CPRORESPEM=input["CPRORESPEM"]
    CC_project_lead=input["CC_project_lead"]
    Cs_LCDT_of_PR_D=input["Cs_LCDT_of_PR_D"]
    Cs_project_lead_ID=input["Cs_project_lead_ID"]
    Cs_previous_person_responsible_ID=input["Cs_previous_person_responsible_ID"]
    Cs_previous_project_lead_ID=input["Cs_previous_project_lead_ID"]
    TPROJECT=input["TPROJECT"]
    TPROPRSTLC=input["TPROPRSTLC"]
    CPROLEAD=input["CPROLEAD"]
    date_for_bamboo=input["date_for_bamboo"]
    bamboo_ID=input["Bamboo_ID_for_Bamboo"]
    emp_id=input["Employee_ID_for_Bamboo"]
    failed_condition_count=[]
    failed_reason_list=[]
    failed_co=[]
    header_values=input["header_values"]
    bamboo_name_id=input["bamboo_name_id"]
    new_project_array=input["new_project_array"]
    values_760=[]

    # for header creation
    try:
        header_values1=header_values.split(",")
        headers={
            
                "column1":header_values1[0].replace('"',''),
                "column2":header_values1[1],
                "column3":header_values1[2],
                "column4":header_values1[3],
                "column5":header_values1[4],
                "column6":header_values1[5],
                "column7":header_values1[6].replace('"','')
            
        }
        #append to Approver_list
        Approvers_List1_array.append(headers)
    except Exception as e:
        return {
            "error":e
        }    
    try:
        #for each of sap-items
        for sap_items in sap_input:
            converted_input={
                    "CCOMPANY": sap_items.get(CCOMPANY),
                    "CPROFITCTR":sap_items.get(CPROFITCTR),
                    "CPROJECT":sap_items.get(CPROJECT),
                    "CPROPRSTLC":sap_items.get(CPROPRSTLC),
                    "CPRORESPEM":sap_items.get(CPRORESPEM),    #-- CPRORESPEM ----person responsible id
                    "CC_project_lead":sap_items.get(CC_project_lead),  # CY30JTZLLY_BE254491CC --PL--
                    "Cs_LCDT_of_PR_D":sap_items.get(Cs_LCDT_of_PR_D),  # Cs1ANs02665903710D543 ---Last Change Date Time of Person Responsible ID 
                    "Cs_project_lead_ID":sap_items.get(Cs_project_lead_ID), # Cs1ANs03FA7ECB345B3B9 -- Last Change Date Time of Project Lead ID
                    "Cs_previous_person_responsible_ID":sap_items.get(Cs_previous_person_responsible_ID), #Cs1ANs224F913DDFEFA5B -- Previous Person Responsible ID ID
                    "Cs_previous_project_lead_ID":sap_items.get(Cs_previous_project_lead_ID), # Cs1ANs7515DDBE8212D62 --Previous Project Lead ID ID
                    "TPROJECT":sap_items.get(TPROJECT),
                    "TPROPRSTLC":sap_items.get(TPROPRSTLC),
                    "CPROLEAD":sap_items.get(CPROLEAD)
                }
            

            try:
                #last_pl_date declaration from Cs1ANs03FA7ECB345B3B9
                last_pl_date=converted_input.get("Cs_project_lead_ID")
                # if last_pl_date != None and  len(last_pl_date)!="":
                if last_pl_date != None and  last_pl_date !="":
                    from datetime import datetime
                    input_datetime = datetime.strptime(last_pl_date, "%d.%m.%Y %H:%M:%S UTC")
                    last_pl_date_str = input_datetime.strftime("%Y-%m-%d %H:%M:%S")
                    last_pl_date=datetime.strptime(last_pl_date_str, "%Y-%m-%d %H:%M:%S")
                else:
                    last_pl_date=None
            except Exception as e:
                failed_reason_list.append( f"${e} while creating last_pl_date")
                error_list.append(sap_items)
                continue
            # ------------------------------------
            try:
                #last_pr_date declaration from Cs1ANs02665903710D543
                last_pr_date=converted_input.get("Cs_LCDT_of_PR_D")
                # if last_pr_date != None and  len(last_pr_date)!=0:
                if last_pr_date != None and  last_pr_date !="":
                    from datetime import datetime
                    input_datetime = datetime.strptime(last_pr_date, "%d.%m.%Y %H:%M:%S UTC")
                    last_pr_date_str = input_datetime.strftime("%Y-%m-%d %H:%M:%S")
                    last_pr_date=datetime.strptime(last_pr_date_str, "%Y-%m-%d %H:%M:%S")
                else:
                    last_pr_date=None
            except Exception as e:
                failed_reason_list.append( f"${e} while creating last_pr_date")
                error_list.append(sap_items)
                continue
            # -----------------------------------------
            try:
                #prev_lead declaration from Cs1ANs7515DDBE8212D62
                prev_lead=converted_input.get("Cs_previous_project_lead_ID")
                if prev_lead !=None and len(prev_lead)!=0:
                    prev_lead=prev_lead
                else:
                    prev_lead=None
            except Exception as e:
                failed_reason_list.append( f"${e} while creating prev_lead")
                error_list.append(sap_items)
                continue


            # --------------------------------------
            try:
                 #prev_resp declaration from Cs1ANs224F913DDFEFA5B
                prev_resp=converted_input.get("Cs_previous_person_responsible_ID")
                if prev_resp !=None and len(prev_resp)!=0:
                    prev_resp=prev_resp
                else:
                    prev_resp=None
            except Exception as e:
                failed_reason_list.append( f"${e} while creating prev_resp")
                error_list.append(sap_items)
                continue
            #-------------------------------------------
            try:
                # proj_lead declaration CY30JTZLLY_BE254491CC
                proj_lead=converted_input.get("CC_project_lead")
                if proj_lead !=None and len(proj_lead)!=0:
                    proj_lead=proj_lead
                else:
                    proj_lead=None
            except Exception as e:
                failed_reason_list.append( f"${e} while creating proj_lead")
                error_list.append(sap_items)
                continue
            # ------------------------------------------
            try:
                #PRF declaration from CPRORESPEM changed to CPROLEAD 
                PRF=converted_input.get("CPROLEAD")
                if PRF !=None and len(PRF)!=0:
                    PRF=PRF
                else:
                    PRF=None
            except Exception as e:
                failed_reason_list.append( f"${e} while creating PRF")
                error_list.append(sap_items)
                continue
           
            try:
                 #----------------------------------------new project----------
                Project_Lead=None
                if sap_items in new_project_array:
                    #If SAP Project Lead is populated, then write SAP Project Lead as Project Approver for Concur. 
                    # If SAP Project Lead [blank], then write SAP Person Responsible For as Project Approver in Concur.
                    if proj_lead!= None and len(proj_lead) >0 :
                        #calling 710 method to add
                        result_710=for_710(proj_lead,bamboo_input,emp_id,bamboo_name_id,bamboo_ID,date_for_bamboo,converted_input)   # proj_lead=PL
                        called_count_710=called_count_710+1
                        if result_710.get("error")!=None:
                            failed_reason_list.append(result_710.get("error"))
                            error_list.append(sap_items)
                        if result_710.get("Approvers_List")!=None:
                            Approvers_List1_array.append(result_710.get("Approvers_List"))
                        continue
                    else:
                        called_count_710=called_count_710+1
                        #calling 710 method to add
                        result_710=for_710(PRF,bamboo_input,emp_id,bamboo_name_id,bamboo_ID,date_for_bamboo,converted_input)
                        if result_710.get("error")!=None:
                            failed_reason_list.append(result_710.get("error"))
                            result_710.append(sap_items)
                        if result_710.get("Approvers_List")!=None:
                            Approvers_List1_array.append(result_710.get.get("Approvers_List"))
                        continue
                        
                #--------------------------------------Modified project--------PRF=person responsible id----  proj_lead=PL
                #1. If PRF and PL are populated and both are changed to new names on same day, 
                    # then send delete for previous PL and add for new PL only.
                if (proj_lead!= None and len(proj_lead) >0) and (PRF!= None and len(PRF) >0):
                    if (last_pr_date!=None and last_pl_date!=None):
                        if (last_pr_date==last_pl_date):
                            values_760.append({"condition":1,"items":sap_items,"emp":prev_lead,"emp_type":"prev_lead"})
                            called_count_760=called_count_760+1
                            #calling 760 method to add
                            result=for_760(prev_lead,bamboo_input,emp_id,bamboo_name_id,bamboo_ID,date_for_bamboo,converted_input)
                            if result.get("error")!=None:
                                failed_reason_list.append(result.get("error"))
                                error_list.append(sap_items)
                            if result.get("Approvers_List")!=None:
                                Approvers_List1_array.append(result.get("Approvers_List"))


                            called_count_710=called_count_710+1
                            #calling 710 method to add
                            result_710=for_710(proj_lead,bamboo_input,emp_id,bamboo_name_id,bamboo_ID,date_for_bamboo,converted_input)
                            if result_710.get("error")!=None:
                                failed_reason_list.append(result_710.get("error"))
                                error_list.append(sap_items)
                            if result_710.get("Approvers_List")!=None:
                                Approvers_List1_array.append(result_710.get("Approvers_List"))
                            continue
                  
                from datetime import datetime
                current_date_time = datetime.now()
                today_date = current_date_time.date()
                #2 If PRF and PL are populated and only PL is changed today, then send delete for previous PL and add for new PL only.
                if (proj_lead!= None and len(proj_lead) >0) and (PRF!= None and len(PRF) >0):
                    if (last_pl_date!=None):
                        if (last_pl_date.date()==today_date):
                            values_760.append({"condition":2,"items":sap_items,"emp":prev_lead,"emp_type":"prev_lead"})
                            called_count_760=called_count_760+1
                            #calling 760 method to add
                            result=for_760(prev_lead,bamboo_input,emp_id,bamboo_name_id,bamboo_ID,date_for_bamboo,converted_input)
                            if result.get("error")!=None:
                                failed_reason_list.append(result.get("error"))
                                error_list.append(sap_items)
                            if result.get("Approvers_List")!=None:
                                
                                Approvers_List1_array.append(result.get("Approvers_List"))

                            called_count_710=called_count_710+1
                            #calling 710 method to add
                            result_710=for_710(proj_lead,bamboo_input,emp_id,bamboo_name_id,bamboo_ID,date_for_bamboo,converted_input)
                            if result_710.get("error")!=None:
                                failed_reason_list.append(result_710.get("error"))
                                error_list.append(sap_items)
                            if result_710.get("Approvers_List")!=None:
                                Approvers_List1_array.append(result_710.get("Approvers_List"))
                            continue
                
                #3 If PRF and PL are populated and only PRF is changed today, then don't send anything.
                if (proj_lead!= None and len(proj_lead) >0) and (PRF!= None and len(PRF) >0):
                    if (last_pr_date!=None):
                        if (last_pr_date.date()==today_date):
                            continue
                
                # 4 If PRF is populated and PL is [blank] and PRF is changed today, then send delete for previous PRF and 
                    # add for new PRF only
                # if (PRF!= None and len(PRF) >0) and (proj_lead== None ):
                #     if (last_pr_date!=None):
                #         if (last_pr_date.date()==today_date):
                #             values_760.append({"condition":4,"items":sap_items,"emp":prev_resp,"emp_type":"prev_resp"})
                #             called_count_760=called_count_760+1
                #             #calling 760 method to add
                #             result=for_760(prev_resp,bamboo_input,emp_id,bamboo_name_id,bamboo_ID,date_for_bamboo,converted_input)
                #             if result.get("error")!=None:
                #                 failed_reason_list.append(result.get("error"))
                #                 error_list.append(sap_items)
                #             if result.get("Approvers_List")!=None:
                                
                #                 Approvers_List1_array.append(result.get("Approvers_List"))

                #             called_count_710=called_count_710+1
                #             #calling 710 method to add
                #             result_710=for_710(PRF,bamboo_input,emp_id,bamboo_name_id,bamboo_ID,date_for_bamboo,converted_input)
                #             if result_710.get("error")!=None:
                #                 failed_reason_list.append(result_710.get("error"))
                #                 error_list.append(sap_items)
                #             if result_710.get("Approvers_List")!=None:
                #                 Approvers_List1_array.append(result_710.get("Approvers_List"))
                #             continue
                
                #5. If PRF is populated and PL is [blank] and PL is changed to populated today, then send delete for PRF and
                #     add for new PL.
                # if (PRF!= None and len(PRF) >0) and (proj_lead!= None):                      # DISABLED
                #     if (last_pl_date!=None):
                #         if (last_pl_date.date()==today_date):
                #             called_count_760=called_count_760+1
                #             values_760.append({"condition":5,"items":sap_items,"emp":prev_resp,"emp_type":"prev_resp"})
                #             result=for_760(prev_resp,bamboo_input,emp_id,bamboo_name_id,bamboo_ID,date_for_bamboo,converted_input)
                #             if result.get("error")!=None:
                #                 failed_reason_list.append(result.get("error"))
                #                 error_list.append(sap_items)
                #             if result.get("Approvers_List")!=None:
                                
                #                 Approvers_List1_array.append(result.get("Approvers_List"))

                #             called_count_710=called_count_710+1
                #             result_710=for_710(proj_lead,bamboo_input,emp_id,bamboo_name_id,bamboo_ID,date_for_bamboo,converted_input)
                #             if result_710.get("error")!=None:
                #                 failed_reason_list.append(result_710.get("error"))
                #                 error_list.append(sap_items)
                #             if result_710.get("Approvers_List")!=None:
                #                 Approvers_List1_array.append(result_710.get("Approvers_List"))
                #             continue                                                                   # DISABLED
                            

                #6. If PRF and PL are populated and PL is changed to be [blank] today, then send delete for previous PL and add for PRF.
                if (PRF!= None and len(PRF) >0) and (proj_lead== None):
                    if (last_pl_date!=None) and  (last_pl_date.date()==today_date):
                        values_760.append({"condition":6,"items":sap_items,"emp":prev_lead,"emp_type":"prev_lead"})
                        
                        called_count_760=called_count_760+1
                        #calling 760 method to add
                        result=for_760(prev_lead,bamboo_input,emp_id,bamboo_name_id,bamboo_ID,date_for_bamboo,converted_input)
                        if result.get("error")!=None:
                            failed_reason_list.append(result.get("error"))
                            error_list.append(sap_items)
                        if result.get("Approvers_List")!=None:
                        
                            Approvers_List1_array.append(result.get("Approvers_List"))

                        called_count_710=called_count_710+1
                        #calling 710 method to add
                        result_710=for_710(PRF,bamboo_input,emp_id,bamboo_name_id,bamboo_ID,date_for_bamboo,converted_input)
                        if result_710.get("error")!=None:
                            failed_reason_list.append(result_710.get("error"))
                            error_list.append(sap_items)
                        if result_710.get("Approvers_List")!=None:
                            Approvers_List1_array.append(result_710.get("Approvers_List"))
                        continue
                        

                #7. If PRF and PL are populated and PL is changed to be [blank] and PRF is also changed today,
                #  then send delete for previous PL and add for PRF.
                if (PRF!= None and len(PRF) >0) and (proj_lead== None):
                    if (last_pr_date!=None):
                        if (last_pr_date.date()==today_date):
                            #calling 760 method to add
                            values_760.append({"condition":7,"items":sap_items,"emp":prev_lead,"emp_type":"prev_lead"})
                            called_count_760=called_count_760+1
                            result=for_760(prev_lead,bamboo_input,emp_id,bamboo_name_id,bamboo_ID,date_for_bamboo,converted_input)
                            if result.get("error")!=None:
                                failed_reason_list.append(result.get("error"))
                                error_list.append(sap_items)
                            if result.get("Approvers_List")!=None:
                                Approvers_List1_array.append(result.get("Approvers_List"))

                            called_count_710=called_count_710+1
                            #calling 710 method to add
                            result_710=for_710(PRF,bamboo_input,emp_id,bamboo_name_id,bamboo_ID,date_for_bamboo,converted_input)
                            if result_710.get("error")!=None:
                                failed_reason_list.append(result_710.get("error"))
                                error_list.append(sap_items)
                            if result_710.get("Approvers_List")!=None:
                                Approvers_List1_array.append(result_710.get("Approvers_List"))
                            continue

            except Exception as e:
                failed_reason_list.append( f"${e} while adding new conditions")
                error_list.append(sap_items)
                continue
           # Returning response to workato 
        return {
            # "Approvers_List2_array":Approvers_List2_array,
            "Approvers_List1_array":Approvers_List1_array,
            "error_list":error_list,
            "failed_condition_count":failed_condition_count,
            "failed_reason_list":failed_reason_list,
            "failed_co":failed_co,
            "called_times":values_760

            # "called_times":f"{called_count_710},{called_count_760},{matched_760}"
        }
    except Exception as e:
        return {
            "error_list":f"{e} in catch block"
        }
        #test ytest