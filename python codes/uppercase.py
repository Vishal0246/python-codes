str1 = input("Please Enter your Own String : ")
str2 = ''
i = 0
while(i < len(str1)):
    if (str1[i] >= 'a' and str1[i] <= 'z'):
        str2 = str2 + chr((ord(str1[i]) - 32))
    else:
        str2 = str2 + str1[i]
    i = i + 1
print("String in uppercase =  ", str2) 
