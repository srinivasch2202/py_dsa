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
n=float(input())
# the problem is we cant perform for decimal or float values if we take float we cant perform loop
# how to take 2.5^2.5