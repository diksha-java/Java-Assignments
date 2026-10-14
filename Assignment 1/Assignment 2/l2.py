def sort_tuple(tup):
    sorted_list=sorted(tup)
    return tuple(sorted_list)
Tuple=(2,4,6,1,4,7.8,2.7)
result=sort_tuple(Tuple)
print("Original Tuple:",Tuple)
print("Sorted Tuple:",result)
