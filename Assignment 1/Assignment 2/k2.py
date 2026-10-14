n=int(input("Enter the limit:"))
result=[]
for i in range(1,n+1):
    result.append((i,i*i))
print("List of tuples:",result)