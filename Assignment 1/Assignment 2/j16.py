list1=["Hello"," ","world"," ","python"," "]
new_list=[]
for i in list1:
    if i!=" ":
        new_list.append(i)
        print("After removing empty strings:",new_list)