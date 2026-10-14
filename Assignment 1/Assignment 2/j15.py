n=int(input("Enter number of elements:"))
my_list=[]
for i in range(n):
    num=int(input("Enter element:"))
    my_list.append(num)
    my_list[0],my_list[-1]=my_list[-1],my_list[0]
print("List after interchanging first and last elements:",my_list)