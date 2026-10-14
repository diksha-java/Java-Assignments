num=int(input("Enter a number:"))
temp=numsum=0
while temp>0:
    digit=temp % 10
    sum+=digit**3
    temp//=10
    if sum==num:
        print(num,"is an Armstrong number")
    else:
        print(num,"is an not armstrong number")