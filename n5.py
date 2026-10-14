str1=input("Enter a string:")
vowels={'a','e','i','o','u'}
s=set(str1.lower())
if vowels<=s:
    print("The string contains all vowels")
else:
    print("The string does not contain all vowels")