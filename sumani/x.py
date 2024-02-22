# def main(input):

#     ip_address = input["json_file"]
#     try:
#     	x=(input['response']["soap-env:Envelope"][0]["soap-env:Body"][0]["n0:SupplierInvoiceBundleMaintainConfirmation_sync"][0].get('Log')[0].get('Item'))
	
#     except:
# 		return {"error":"Could not find the path"}
	
# 	final_log=""
# 	for item in x:
# 		Note=None
# 		SeverityCode:None
# 		try:
# 			Note=item.get('Note')[0].get("content_")
# 		except:
# 			Note="Not Found"
# 		try:
# 			SeverityCode=item.get('SeverityCode')[0].get("content_")
# 		except:
# 			SeverityCode="Not Found"
# 		log=f"SeverityCode:{SeverityCode};Note:{Note}"
# 	return {"output":final_log}	

# import re
# def main(input):
#     input1 = input["json_file"]
#     try:
#         print()
#         x = (input1['response']["soap-env:Envelope"][0]["soap-env:Body"][0]["n0:SupplierInvoiceBundleMaintainConfirmation_sync"][0].get('Log')[0].get('Item'))
#     except:
#         return {"error": "could not find the path"}

#     final_log = ""
#     array_of_note=[]
#     dublicateString="duplicate of invoice"
#     invoice_numbers=" "
#     dublicate_present=False
#     SeverityCode_for_dublicate=0
#     for item in x:
#         Note = None
#         SeverityCode = None
#         try:
#             Note = item.get('Note')[0].get("content_")
#         except:
#             Note = "Not Found"
#         try:
#             SeverityCode = item.get('SeverityCode')[0].get("content_")
#         except:
#             SeverityCode = "Not Found"
        
#         if dublicateString in Note:
#             pattern = re.compile(r'\b[A-Z0-9]+-\d+\b')
#             match = re.search(pattern, Note)
#             if match:
#                 dublicate_present=True
#                 SeverityCode_for_dublicate=SeverityCode
#                 extracted_pattern = match.group(0)
#                 invoice_numbers+=f"{extracted_pattern},"
#             else:
#                 log = f"SeverityCode:{SeverityCode};Note:{Note}"
#                 # words = Note.split()
#                 # if ' '.join(words[:6]) not in array_of_note:
#                 final_log += log + "\n"
#                 # array_of_note.append(' '.join(words[:6]))
#         else:
#             log = f"SeverityCode:{SeverityCode};Note:{Note}"
#             final_log += log + "\n"
        
#     if dublicate_present:
#         log2=f"SeverityCode:{SeverityCode_for_dublicate};Note:Invoice may be a duplicate of invoice{invoice_numbers}"
#         final_log += log2 + "\n"
#     return {"output": final_log}


import re
def main(input):
    input1 = input["json_file"]
    # get input from workato
    try:
        items = (input1['response']["soap-env:Envelope"][0]["soap-env:Body"][0]["n0:SupplierInvoiceBundleMaintainConfirmation_sync"][0].get('Log')[0].get('Item'))
        # get items from items
    except:
        return {"error": "could not find the path"}
    # returning error in case of path changed

    final_log = ""
    array_of_note=[]
    dublicateString="duplicate of invoice"
    dublicateStringforMemo="Credit memo may be a duplicate"
    invoice_numbers=" "
    invoice_numbers_for_credit_memo=" "
    dublicate_present=False
    dublicate_present_for_credit=False
    SeverityCode_for_dublicate=0
    # for each of items
    for item in items:
        Note = None
        SeverityCode = None
        try:
            Note = item.get('Note')[0].get("content_")
            # fluck log
        except:
            Note = "Not Found"
            # if content not found
        try:
            SeverityCode = item.get('SeverityCode')[0].get("content_")
            # flucking sevierity code
        except:
            SeverityCode = "Not Found"
            # if sevierity code not found
        
        if dublicateString in Note or dublicateStringforMemo in Note:
            # validation for dublicate string in Credit memo 
            pattern = re.compile(r'\b[A-Z0-9]+-\d+\b')
            # regex for get invoice number
            match = re.search(pattern, Note)
            if match:
                # if we get invoice number
                if dublicateString in Note:
                    dublicate_present=True
                    SeverityCode_for_dublicate=SeverityCode
                    extracted_pattern = match.group(0)
                    invoice_numbers+=f"{extracted_pattern},"
                else:
                    # for credit memo
                    dublicate_present_for_credit=True
                    extracted_pattern = match.group(0)
                    invoice_numbers_for_credit_memo+=f"{extracted_pattern},"
                    # adding to invoice_numbers_for_credit_memo
            else:
                log = f"SeverityCode:{SeverityCode};Note:{Note}"
                # words = Note.split()
                # if ' '.join(words[:6]) not in array_of_note:
                final_log += log + "\n"
                # adding to logger
                # array_of_note.append(' '.join(words[:6]))
        else:
            log = f"SeverityCode:{SeverityCode};Note:{Note}"
            final_log += log + "\n"
        
    if dublicate_present:
        # if dublicate invoices found adding to final logger
        log2=f"SeverityCode:{SeverityCode_for_dublicate};Note:Invoice may be a duplicate of invoice{invoice_numbers}"
        final_log += log2 + "\n"
    if dublicate_present_for_credit:
        # if dublicate invoices found adding to final logger
        log3=f"SeverityCode:{SeverityCode_for_dublicate};Note:Credit memo may be a duplicate of credit memo{invoice_numbers_for_credit_memo}"
        final_log += log3 + "\n"
    return {"output": final_log}
#   returning output
 