import json
from datetime import datetime
def main(input):

    sap_input = input["sap_input"]
    bamboo_input=input["bamboo_item"]
    Approvers_List1_array=[]
    Approvers_List2_array=[]
    try:
        for sap_items in sap_input:
            converted_input={
                    "CCOMPANY": sap_items.get("CCOMPANY"),
                    "CPROFITCTR":sap_items.get("CPROFITCTR"),
                    "CPROJECT":sap_items.get("CPROJECT"),
                    "CPROPRSTLC":sap_items.get("CPROPRSTLC"),
                    "CPRORESPEM":sap_items.get("CPRORESPEM"),
                    "CC_project_lead":sap_items.get("CY30JTZLLY_BE254491CC"),
                    "Cs_LCDT_of_PR_D":sap_items.get("Cs1ANs02665903710D543"),
                    "Cs_project_lead_ID":sap_items.get("Cs1ANs03FA7ECB345B3B9"),
                    "Cs_previous_person_responsible_ID":sap_items.get("Cs1ANs224F913DDFEFA5B"),
                    "Cs_previous_project_lead_ID":sap_items.get("Cs1ANs7515DDBE8212D62"),
                    "TPROJECT":sap_items.get("TPROJECT"),
                    "TPROPRSTLC":sap_items.get("TPROPRSTLC")
                }
            last_pl_date=converted_input.get("Cs_previous_person_responsible_ID")
            if last_pl_date != None and  len(last_pl_date)!=0:
                input_datetime = datetime.strptime(last_pl_date, "%d.%m.%Y %H:%M:%S UTC")
                last_pl_date = input_datetime.strftime("%Y-%m-%d %H:%M:%S")
            else:
                last_pl_date=None
            # ------------------------------------

            last_pr_date=converted_input.get("Cs_previous_person_responsible_ID")
            if last_pr_date != None and  len(last_pr_date)!=0:
                input_datetime = datetime.strptime(last_pr_date, "%d.%m.%Y %H:%M:%S UTC")
                last_pr_date = input_datetime.strftime("%Y-%m-%d %H:%M:%S")
            else:
                last_pr_date=None
            # -----------------------------------------

            prev_lead=converted_input.get("Cs_previous_project_lead_ID")
            if prev_lead !=None and len(prev_lead)!=0:
                prev_lead=prev_lead
            else:
                prev_lead=None


            # --------------------------------------
            prev_resp=converted_input.get("Cs_previous_person_responsible_ID")
            if prev_resp !=None and len(prev_resp)!=0:
                prev_resp=prev_resp
            else:
                prev_resp=None
            #-------------------------------------------
            proj_lead=converted_input.get("CC_project_lead")
            if proj_lead !=None and len(proj_lead)!=0:
                proj_lead=proj_lead
            else:
                proj_lead=None
            # ------------------------------------------
            pro_lead=converted_input.get("CPRORESPEM")
            if pro_lead !=None and len(pro_lead)!=0:
                pro_lead=pro_lead
            else:
                pro_lead=None
            # -------------------------------------------Previous_Lead----------
            if (last_pl_date is not None and last_pr_date is not None) and (last_pl_date >= last_pr_date and (prev_lead is not None and len(prev_lead) > 0)):
                Previous_Lead=prev_lead
            elif(last_pl_date is not None and last_pr_date is not None) and (last_pl_date > last_pr_date and (prev_lead is not None and len(prev_lead) > 0)):
                Previous_Lead=prev_lead
            elif(last_pr_date is not None and last_pl_date is not None) and (last_pr_date > last_pl_date and (prev_lead is not None and prev_lead == 0)):
                Previous_Lead=None
            elif(proj_lead is not None and len(proj_lead)==0) and ((last_pr_date is not None and last_pl_date is not None) and last_pr_date>last_pl_date ):
                Previous_Lead=prev_resp
            elif(prev_lead is not None and len(prev_lead)>0) and ((last_pr_date is not None and last_pl_date is not None) and last_pr_date==last_pl_date ):
                Previous_Lead=prev_lead
            elif(prev_lead is not None and len(prev_lead)==0) and ((last_pr_date is not None and last_pl_date is not None) and last_pr_date>=last_pl_date ):
                Previous_Lead=prev_resp
            else:
                Previous_Lead=prev_lead

            # -----------------------------------------------Project_Lead-------
            if(proj_lead is not None and len(proj_lead)>0) and ((last_pr_date is not None and last_pl_date is not None) and last_pl_date>=last_pr_date ):
                Project_Lead=proj_lead
            elif(proj_lead is not None and len(proj_lead)==0) and ((last_pr_date is not None and last_pl_date is not None) and last_pr_date>=last_pl_date ):
                Project_Lead=pro_lead
            elif(proj_lead is not None and len(proj_lead)>0) and ((last_pr_date is not None and last_pl_date is not None) and last_pr_date>=last_pl_date ):
                Project_Lead=pro_lead
            elif(proj_lead is not None and len(proj_lead)>0) and ((last_pr_date is not None and last_pl_date is not None) and last_pl_date>last_pr_date ):
                Project_Lead=proj_lead
            elif(proj_lead is not None and len(proj_lead)>0) and ((last_pr_date is not None and last_pl_date is not None) and last_pr_date>last_pl_date ):
                Project_Lead=proj_lead
            elif(proj_lead is not None and len(proj_lead)==0) and ((last_pr_date is not None and last_pl_date is not None) and last_pl_date>last_pr_date ):
                Project_Lead=pro_lead
            else:
                Project_Lead=proj_lead

            if (Project_Lead !=Previous_Lead):
                empid=None if Previous_Lead == None else Previous_Lead   #-----------verify

            bamboo_list=bamboo_input
            for items in bamboo_list:
                if items.get("CZ8A3365DF41600F8C")==empid:
                    Bamboo_ID=items.get("CZ0CD8A563121AD221")
                    Employee_ID=items.get("CZ8A3365DF41600F8C")
                    Employee_Text=items.get("TZ8A3365DF41600F8C")
                    break
    
            if (Employee_ID != None ):
                prev_employee=Employee_ID
            else:
                prev_employee=empid

            Approvers_List={
                "column1":"760,PMT",
                "column2":prev_employee,
                "column3":converted_input.get("CCOMPANY"),
                "column4":converted_input.get("CPROFITCTR"),
                "column5":converted_input.get("CPROJECT"),
                "column6":None,
                "column7":None,
                "column8":None,
                "column9":None,
                "column10":None,
                "column11":None,
                "column12":None  
            }
            Approvers_List1_array.append(Approvers_List)


            empid2=Project_Lead


            Bamboo_ID=None
            Employee_ID=None
            Employee_Text=None
            for items in bamboo_list:
                if items.get("CZ8A3365DF41600F8C")==empid2:
                    Bamboo_ID=items.get("CZ0CD8A563121AD221")
                    Employee_ID=items.get("CZ8A3365DF41600F8C")
                    Employee_Text=items.get("TZ8A3365DF41600F8C")
                    break
        # -------------------------
            if (Employee_ID !=None):
                employee=Employee_ID
            else:
                employee=empid2

                if converted_input.get("TPROPRSTLC")=="Closed":
                    Approvers_List2={
                                "column1":"760,PMT",
                                "column2":prev_employee,
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
                                "column15":None,
                                "column16":None
                            }
                    Approvers_List2_array.append(Approvers_List2)
        return {
            "Approvers_List2_array":Approvers_List2_array,
            "Approvers_List1_array":Approvers_List1_array
        }
    except Exception as e:
        return {
            "error":e
        }