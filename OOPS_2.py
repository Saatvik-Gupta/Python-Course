'''
INHERITANCE and its Types---

1).Single Inheritance
2).Multilevel Inheritance
3).Multiple Inheritance
4).Heriarchal Inheritanve
'''

class Inheritance_demo:  #Parent calss
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def sum(self):
        print(f"Sum of {self.a} and {self.b} is {self.a+self.b} ")

    def difference(self):
        print(f"Subtraction of {self.a} and {self.b} is {self.a-self.b} ")    

class child_demo(Inheritance_demo):   #Child class of parent class
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def multiply(self):
        print(f"Multiplication of {self.a} and {self.b} is {self.a*self.b} ")

    def divide(self):
        print(f"Division of {self.a} and {self.b} is {self.a/self.b} ") 

c=int(input("Enter First number:"))
d=int(input("Enter Seconf number:"))
obj=child_demo(c,d)
obj.sum()
obj.difference()
obj.multiply()
obj.divide()               
        
