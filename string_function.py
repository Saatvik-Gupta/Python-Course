#------.string functions

a="Saatvik Project"
b=" Saatvik Working On String Functions "

print(a.upper(),a.lower())
print(a.isdigit(),a.isupper(),a.islower(),a.isalnum())
print(a.capitalize())#only first string word letter is capital
print(a.title())#all words first letter in string is capital
print(b.strip())#l+r whitespaces remove
print(b.lstrip(),b.rstrip())#l,r " "remove 
print(b.ljust(8),b.rjust(8))
print(a.count("a"))
print(b.endswith(" "))
print(a.startswith("S"))
print(a.split())
print(a.split('i'))
print(a.find("z")) #if not foundd retrun -1
print(a.index("a")) #if nor found return error
print(a.casefold()) #just like .lower() but for special character returns some different value rather than the character itself"""

