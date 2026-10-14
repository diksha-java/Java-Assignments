def tuple_to_string(tup):
    result=''.join(tup)
    return result
n=int(input("Enter number of elements:"))
lst = []
for i in range(n):
 value=input("Enter element:")
 lst.append(value)
 tup=tuple(lst)
 string_result=tuple_to_string(tup)
 print("Tuple:",tup)
 print("String:",string_result)
