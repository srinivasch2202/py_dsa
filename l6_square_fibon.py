# a^n
# a=5
# n=2

# 5^2=25
# 3^4=81


a=int(input("enter the a"))
n=int(input("enter the n"))
s=1
for i in range(1,n+1):
    s*=a
print(s)  
# n=float(input())
# the problem is we cant perform for decimal or float values if we take float we cant perform loop
# how to take 2.5^2.5

# fibonacci series 0,1,1,2,3,4,8,13
                #  1,2,3,4,5,6,7,8
# series is prevous of sum of two current

n=int(input("enter the number"))
a=0
b=1
next_num=0
c=1
while(c<=n):
    print(next_num)
    a=b
    b=next_num
    next_num=a+b
    c+=1

# other methods



