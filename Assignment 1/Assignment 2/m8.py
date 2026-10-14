n=int(input("Enter a number:"))
square_dict={}
for x in range(1,n+1):
    square_dict[x]=x * x
print("Generated Dictionary:")
print(square_dict)