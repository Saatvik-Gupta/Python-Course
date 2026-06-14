#This is single line comment
"""This is multiline comment in python
also use ctrl is / for comment multiple lines a time"""
#Code for strings:

#--------.reverse a string and removing nth index character

string=input("Enter the String:")
n=int(input("Enter the nth index:"))

newstr=string[:n]+string[n+1:]
reverse=string[::-1]

print("Original string is {}".format(string))
print("Updated nth removal string is {}".format(newstr))
print("Reversed string is {}".format(reverse))


