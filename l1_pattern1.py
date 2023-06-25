"""
----p1
if n=2 we have to print XX
                        XX
if n==3 XXX
        XXX
        XXX
note:-we have to find the relation between rows and columns
----p2

        X
    X       X
X       X       X        n==3
    X       X              r=2n-1 
        X                   no of rows are 5

----p3

"""
n=int(input("enter the number"))
for i in range(n):
    for i in range(n):
        print("x",end=" ")
    print("\n")

n=int(input("enter the number"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(i,end=" ")
    print("\n")


# next problem
# n=int(input("enter the number"))
# n1=2*n-1
# for i in range(1,n1+1):
#     for j in range(1,n1+1,2):
#         print("X"*j)
    