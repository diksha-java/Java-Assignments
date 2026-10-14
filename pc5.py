import string
text=input("Enter a string:")
result=" "
for ch in text:
    if ch in string.punctuation:
        result+="#"
    else:
        result+=ch
print("Modified string:",result)