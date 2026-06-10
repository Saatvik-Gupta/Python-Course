'''
Understanding---
classes,object,constructor,static method,inheritance etc
'''

class CollegeToppers:   #class is a blueprint of creating and object
    def __init__(self,name,classname,roll_no,per):
        self.name=name
        self.classname=classname
        self.roll_no=roll_no
        self.per=per

    def show(self):
        print(f'''Name: {self.name}
              Class:{self.classname}
              Roll No.:{self.roll_no}
              Percentage:{self.per}%''')
                                            
while(True):

    for i in range(1,4): #4 students
        n=input(f"Enter Student {i} Name:")
        c=input(f"Enter Student {i} Class:")
        r=int(input(f"Enter Student {i} Roll No.:"))
        p=int(input(f"Enter Student {i} Percent:"))
        print(f"Details of Student {i}---")

        obj=CollegeToppers(n,c,r,p)
        obj.show()  #same as CollegeToppers.show(obj)
        