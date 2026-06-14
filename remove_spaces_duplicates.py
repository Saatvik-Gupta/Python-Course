#-----------.to remove spaces from string and duplicate variables

string=input("Enter the String:")
newstr1=" "
newstr2=" "
for i in string:
    if(i==" "):
        continue
    newstr1=newstr1+i
print(newstr1)  
for i in string:
    if(i not in newstr2):
        newstr2=newstr2+i
    else:
        pass
print(newstr2)

