#-------.checking special character exist or not

string=input("Enter the string bro:")
special=string.isalnum()

if(special==True):

    print("Special character don't exist in {}".format(string))
else:

    print("Special character exist's in {}".format(string))