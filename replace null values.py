def replace_null(input_list):
    ignore_words = ["nil","Nil","NIL","null","Null","NULL"]
    for i in range(len(input_list)):
        # if input_list[i] in ["Null","null","Nil","nil"]:
        if input_list[i] in ignore_words:
            input_list[i]=1
    print(input_list)
    
replace_null([1,2,"Null",4,"Nil",5])
