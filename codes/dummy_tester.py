from datetime import datetime

Approvers_List_array=[]
Approvers_List2_array=[]
input={
		"CCOMPANY": "{\"uri\"=>\"https://my345659.sapbydesign.com/sap/byd/odata/ana_businessanalytics_analytics.svc/RPZ7054C7C00CC39AF5BE9235QueryResults('%7CCCOMPANY%3DNA-01-01%7CCPROFITCTR%3DNA-01-01-BR%7CCPROPRSTLC%3D2%7CCY30JTZLLY_BE254491CC%3D403057%7CCPROJECT%3DF216609%7CCs1ANs7515DDBE8212D62%3D300020%7CCs1ANs224F913DDFEFA5B%3D300725%7CCPRORESPEM%3D300725%7CCs1ANs03FA7ECB345B3B9%3D08.06.2023%2018%3A02%3A12%20UTC%7CCs1ANs02665903710D543%3D01.05.2023%2018%3A57%3A28%20UTC%7C')\", \"type\"=>\"sapbyd.RPZ7054C7C00CC39AF5BE9235QueryResult\"}",
		"CPROFITCTR": "NA-01-01",
		"CPROJECT": "NA-01-01-BR",
		"CPROPRSTLC": "F216609",
		"CPRORESPEM": "2",
		"CY30JTZLLY_BE254491CC": "300725",
		"Cs1ANs02665903710D543": "403057",
		"Cs1ANs03FA7ECB345B3B9": "01.05.2023 18:57:28 UTC",
		"Cs1ANs224F913DDFEFA5B": "08.06.2023 18:02:12 UTC",
		"Cs1ANs7515DDBE8212D62": "300725",
		"TPROJECT": "300020",
		"TPROPRSTLC": "FY23 Carlyle Global Investor Conference"
	}
converted_input={
    "CCOMPANY": input.get("CCOMPANY"),
    "CPROFITCTR":input.get("CPROFITCTR"),
    "CPROJECT":input.get("CPROJECT"),
    "CPROPRSTLC":input.get("CPROPRSTLC"),
    "CPRORESPEM":input.get("CPRORESPEM"),
    "CY 30 JTZLLY BE 254491 CC project lead":input.get("CY30JTZLLY_BE254491CC"),
    "Cs 1 A ns 02665903710 D 543 LCDT of PR D":input.get("Cs1ANs02665903710D543"),
    "Cs 1 A ns 03 FA 7 ECB 345 B 3 B 9 lcdt of project lead ID":input.get("Cs1ANs03FA7ECB345B3B9"),
    "Cs 1 A ns 224 F 913 DDFEFA 5 B previous person responsible ID":input.get("Cs1ANs224F913DDFEFA5B"),
    "Cs 1 A ns 7515 DDBE 8212 D 62 previous project lead ID":input.get("Cs1ANs7515DDBE8212D62"),
    "TPROJECT":input.get("TPROJECT"),
    "TPROPRSTLC":input.get("TPROPRSTLC")
}
# ------------------------------
last_pl_date=converted_input.get("Cs 1 A ns 224 F 913 DDFEFA 5 B previous person responsible ID")
if last_pl_date != None and  len(last_pl_date)!=0:
    input_datetime = datetime.strptime(last_pl_date, "%d.%m.%Y %H:%M:%S UTC")
    last_pl_date_str = input_datetime.strftime("%Y-%m-%d %H:%M:%S")
    last_pl_date=datetime.strptime(last_pl_date_str, "%Y-%m-%d %H:%M:%S")
else:
    last_pl_date=None


# ------------------------------------

last_pr_date=converted_input.get("Cs 1 A ns 224 F 913 DDFEFA 5 B previous person responsible ID")
if last_pr_date != None and  len(last_pr_date)!=0:
    input_datetime = datetime.strptime(last_pr_date, "%d.%m.%Y %H:%M:%S UTC")
    last_pr_date_str = input_datetime.strftime("%Y-%m-%d %H:%M:%S")
    last_pr_date=datetime.strptime(last_pl_date_str, "%Y-%m-%d %H:%M:%S")
else:
    last_pr_date=None
# -----------------------------------------

prev_lead=converted_input.get("Cs 1 A ns 7515 DDBE 8212 D 62 previous project lead ID")
if prev_lead !=None and len(prev_lead)!=0:
    prev_lead=prev_lead
else:
    prev_lead=None
print(prev_lead)

# --------------------------------------
prev_resp=converted_input.get("Cs 1 A ns 224 F 913 DDFEFA 5 B previous person responsible ID")
if prev_resp !=None and len(prev_resp)!=0:
    prev_resp=prev_resp
else:
    prev_resp=None
#-------------------------------------------
proj_lead=converted_input.get("CY 30 JTZLLY BE 254491 CC project lead")
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
elif(last_pr_date is not None and last_pl_date is not None) and (last_pr_date > last_pl_date and (prev_lead is not None and len(prev_lead) == 0)):
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
    empid=None if Previous_Lead == None else Previous_Lead

    # -----------------------------------------get list input-------------------
    bamboo_list=[{
				"__metadata": {
					"uri": "https://my345659.sapbydesign.com/sap/byd/odata/ana_businessanalytics_analytics.svc/RPZ965CA139E2959145E1E187QueryResults('%7CCZ0CD8A563121AD221%3D101%7CCZ8A3365DF41600F8C%3D300001%7C')",
					"type": "sapbyd.RPZ965CA139E2959145E1E187QueryResult"
				},
				"CZ0CD8A563121AD221": "101",
				"CZ8A3365DF41600F8C": "300001",
				"TZ8A3365DF41600F8C": "Maureen Ryan Fable Fable"
			},
			{
				"__metadata": {
					"uri": "https://my345659.sapbydesign.com/sap/byd/odata/ana_businessanalytics_analytics.svc/RPZ965CA139E2959145E1E187QueryResults('%7CCZ0CD8A563121AD221%3D1012%7CCZ8A3365DF41600F8C%3D390028%7C')",
					"type": "sapbyd.RPZ965CA139E2959145E1E187QueryResult"
				},
				"CZ0CD8A563121AD221": "1012",
				"CZ8A3365DF41600F8C": "390028",
				"TZ8A3365DF41600F8C": "Adam L Haer"
			},
			{
				"__metadata": {
					"uri": "https://my345659.sapbydesign.com/sap/byd/odata/ana_businessanalytics_analytics.svc/RPZ965CA139E2959145E1E187QueryResults('%7CCZ0CD8A563121AD221%3D1013%7CCZ8A3365DF41600F8C%3D300002%7C')",
					"type": "sapbyd.RPZ965CA139E2959145E1E187QueryResult"
				},
				"CZ0CD8A563121AD221": "1013",
				"CZ8A3365DF41600F8C": "300002",
				"TZ8A3365DF41600F8C": "Elizabeth E Zacharias"
			}]
    
    Bamboo_ID=None
    Employee_ID=None
    Employee_Text=None
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

    if (len(prev_employee)> 0 and  prev_employee != None):
        if converted_input.get("TPROPRSTLC")!="Closed":
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
                
            Approvers_List_array.append(Approvers_List)



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
            

print(Approvers_List2_array)
print(Approvers_List_array)








