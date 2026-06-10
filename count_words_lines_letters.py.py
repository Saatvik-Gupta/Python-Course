#---------To calculate number of lines,words and letters from a file

def calculation(val):
    words=0;line=0;letter=0
    letter=len(val)  #length of string
    words=len(val.split()) #split gives a list of seperataed by spaces identifying words
    line=val.count("\n") +1 if(val) else 0
    print("No. of words:",words)
    print(line)
    print(letter)

f=open("C:\\Users\\shobh\\OneDrive\\Desktop\\sourcefile.txt","r")
content=f.read()
f.close()
calculation(content)