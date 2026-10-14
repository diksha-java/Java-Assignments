t=(1,2,3,2,4,1,5)
repeated=[]
for item in t:
    if t.count(item)>1 and item not in repeated:
        repeated.append(item)
        unique=tuple(set(t))
print("Original tuple:",t)
print("Repeated items:",repeated)
print("Updated tuple:",unique)