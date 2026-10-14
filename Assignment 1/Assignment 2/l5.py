n=int(input("Enter number of elements:"))
lst=[]
for i in range(n):
    value=int(input("Enter element:"))
    lst.append(value)
    tup=tuple(lst)
print("Tuple:",tup)
item=int(input("Enter element to search:"))
if item in tup:
 print("Element exists in the tuple.")
else:
 print("Element does not exist in the tuple.")