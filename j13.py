list1=[10,20,30,20,40,20]
remove_element=20
new_list=[]
for i in list1:
    if i!=remove_element:
        new_list.append(i)
print("List after removing element:",new_list)
