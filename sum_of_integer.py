# how to find the sum of digit
# if input is 123 output should be 6
# if somehow we get each digit the problem is sloved

print(123%10)#remainder
print(123//10)#quatiet
n=int(input("enter the number "))
s=0
while True:
    if  (n <=0):
        print(s)
        break
    else:
        r=n%10
        s+=r
        n=n//10


 
n=int(input("enter"))
s=0
while (n>0):# if condition fails
    r=n%10
    s+=r
    n=n//10
print(s)

# what if number is negative and what if i need specfic number should add
# in java u should change data type for long number


# string based approach 
# ord,chr
print(ord("a"))
print(chr(97))

n=int(input("enter the num"))
# n=str(n)
s=0
for i in str(n):
    s+=int(i)
print(s)

n=str(int(input("enter the number")))
print(type(n)) 
# little different from java
# we have to subtract 48 from 
print((ord("1")-48))#another approach

