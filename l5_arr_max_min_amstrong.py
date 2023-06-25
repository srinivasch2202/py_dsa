# fixed array length is 5
l=[5,4,9,-1,2]
# we have to select 4 elements such that sum is maximux
"""
5 4 9 -1  == 17
4 9 -1 2  == 14
9 -1 2 5  == 15
-1 2 5 4  == 10
2 5 4 9   == 20
only this possibility
min is 10 and max is 20
"""
# question :- from a given array select 4 elements such that there sum is max ,min
# output is 10,20


# my thinking and approach
# if sort and add first 4 digits for min and last 4 for max
l=[5,4,9,-1,2]
l1=sorted(l)
# print(l1)
s=0
for i in range(len(l1)):
    # print(l[i])
    if i <=3:
        s+=l1[i]
    else:
        break
print(s)
# for i in (len(l1)):
    # print(l1[i])
# i am not getting how to iterate over from back
#---------------------------------------------
#time complex if i iterate it will take n time and if i sort it takes nlogn time


l=[4,-1,3,-2,7]
l1=sorted(l,reverse=True)
# i got it how to reverse we have to sort the array in reverse order
"""
4,-1,3,-2=4
-1,3,-2,7=7
3,-2,7,4=12
-2,7,4,-1=8
7,4,-1,3=13

output 4 and 13
"""
s=0
for i in range(len(l1)):
    if i <= 3:
        s+=l1[i]
print(s)

# another approach 
# min=sum of all elements - highest num
# max=sum of all elements - lowest num

# it only applies if it has n numbers and n-1 numbers

# logic  to find max and min elements and its value
s=0
l=[5,4,9,-1,2]
print(sum(l)-min(l)) 

# armstrong number
# n=153 
"""
1^3=1
5^3=125
3^3=27
1+125+27=153
"""
n=153

s=0
for i in str(n):
    # print(i)
    n1=int(i)
    s+=(n1**3)
if s==n:
    print(f"{s} it is amstrong")
else:
    print("not a astromg")

# we can use remainder and quotient menthod to get elements 


# harshad number
n=18 
# when  number is   divided by sum number then it is harshad completely

# 18/9==0 