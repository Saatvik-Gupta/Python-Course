#-----construct a file using try-except to copy contents

try:
    with open("C:\\Users\\shobh\\OneDrive\\Desktop\\sourcefile.txt","r") as f:
        data=f.read()
    with open("C:\\Users\\shobh\\OneDrive\\Desktop\\destination.txt","w") as f1:
        f1.write(data)
    with open("C:\\Users\\shobh\\OneDrive\\Desktop\\destination.txt","r") as f2:
        print(f2.read())
    print("File Successfully copied!")

except FileNotFoundError as e:
    print("No File found and an error {}".format(e))
finally:
    print("End of code:")                 

