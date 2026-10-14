n=int(input("Enter number of elements:"))
lst=[]
for i in range(n):
    value=int(input("Enter element:"))
    lst.append(value)
    tup=tuple(lst)
print("Tuple:",tup)
repeated=[]
for item in tup:
        if tup.count(item)>1 and item not in repeated:
            repeated.append(item)
print("Repeated items:",tuple(repeated))