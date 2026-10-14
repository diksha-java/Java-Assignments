string=input("Enter a string:")
result=' '
vowels="aeiouAEIOU"
for char in string:
    if char not in vowels and char not in result:
        result+=char
print("Modified string:",result)