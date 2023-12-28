def main(input):
    approver_list1 = input["approver_list1"]
    approver_list2 = input["approver_list2"]

    if len(approver_list1)>=len(approver_list2):
        max_list=approver_list1
        approver_list=[{"column13": d["column1"], "column14": d["column2"],"column15": d["column3"], "column16": d["column4"],"column17": d["column5"], "column18": d["column6"],"column19": d["column7"], "column20": d["column8"],"column21": d["column9"], "column22": d["column10"],"column23": d["column11"], "column24": d["column12"],"column25": d["column13"], "column26": d["column14"],"column27": d["column15"], "column28": d["f"]} for d in approver_list2]
    else:
        max_list=approver_list2
        approver_list=[{"column17": d["column1"], "column18": d["column2"],"column19": d["column3"], "column20": d["column4"],"column21": d["column5"], "column22": d["column6"],"column23": d["column7"], "column24": d["column8"],"column25": d["column9"], "column26": d["column10"],"column27": d["column11"], "column28": d["column12"]} for d in approver_list1]


    merged_list = []
    count=0
    lenth=len(approver_list)
    for item in max_list:
        merged_dict = item.copy()
        count1=0
        if count<lenth:
            for item2 in approver_list:
                if count1==count:
                    for key_y, value_y in item2.items():
                        merged_dict[key_y] = value_y
                    merged_list.append(merged_dict)
                count1=count1+1
                
        else:
            for key_y, value_y in approver_list[0].items():
                merged_dict[key_y] = ""
            
            merged_list.append(merged_dict)
        count=count+1   

    return {"merged_list":merged_list}

