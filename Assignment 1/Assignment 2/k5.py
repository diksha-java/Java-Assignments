n=int(input("Enter number of elements in tuple:"))
lst=[]
for i in range(n):
    num=int(input("Enter an element: "))
    lst.append(num)
tup=tuple(lst)
print("Original Tuple:",tup)
item=int(input("Enter an item to add: "))
tup=tup+(item,)
print("Updated Tuple:",tup)