n=int(input("Enter number of elements:"))
lst=[]
for i in range(n):
    value=int(input("Enter element:"))
    lst.append(value)
    tup=tuple(lst)
print("Tuple:",tup)
front_element=tup[3]
last_element=tup[5]
print("3th element from front:",front_element)
print("5th element from last:",last_element)