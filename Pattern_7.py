# Pattern 7:
'''
5 4 3 2 1 ...   1
4 3 2 1  and    1 2   
3 2 1           1 2 3
2 1             1 2 3 4
1               1 2 3 4 5...
'''

n=int(input('enter the Limit:'))
print("-----Pattern 1:-----")
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(j ,end=" ")
    print(" ")

print("-----Pattern 2:-----")
for k in range(1,n+1):
    for l in range(k):
        print(l+1,end=" ")
    print(" ")