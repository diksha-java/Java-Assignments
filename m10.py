keys=['Class-V','Class-VI','Class-VII','Class-VIII']
values=[1,2,2,3]
result={}
for i in range(len(keys)):
    if keys[i] in result:
        result[keys[i]].add(values[i])
    else:
        result[keys[i]]={values[i]}
print(result)