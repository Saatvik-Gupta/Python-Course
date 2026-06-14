# Pattern 6:Pyramid
'''
   *           * * * *           *
  * *      +    * * *  =        * *
 * * *           * *           * * *
* * * *           *           * * * *
                               * * *
                                * *
                                 *
'''


#Upper Pyramid
n=int(input("Enter the limit:"))
for i in range(1,n+1):  #run from 1 to n

    ''' First of all determining spaces and printing them.
    if the input is 4 then 3 spaces firstly as (n-i)---->(4-1)=3'''
    
    print(" "*(n-i),end=" ")
    for j in range(i):
        print("*",end=" ") 
    print(" ") 
        
#lower pyramid

for l in range(n-1,0,-1):
        print(" "*(n-l),end=" ")

        for k in range(l):    
            print("*",end=" ")
        print(" ")    

        

