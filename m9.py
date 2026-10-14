sampleString="w3resource"
sampleString=sampleString.lower()
char_dict={}
for ch in sampleString:
    if ch in char_dict:
        char_dict[ch] +=1
    else:
        char_dict[ch]=1
print("Character Dictionary:")
print(char_dict)