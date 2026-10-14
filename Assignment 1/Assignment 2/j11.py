n=int(input("Enter number of elements:"))
my_list=[]
for i in range(n):
    num=int(input("Enter element:"))
    my_list.append(num)
    element=int(input("Enter element to remove:"))
    result_list=[]
    for item in my_list:
        if item !=element:
            result