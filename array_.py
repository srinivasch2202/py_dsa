"""
array
jow to iterate over array
5

ar=[5 7 3 1 2]
maximux in ar
"""
l=eval(input("enter the list"))
max=0
for i in range(len(l)):
    if max < int(l[i]):
        max=l[i]
print(max)
# it fails if all elements are negative

# here is the correct code
l=eval(input("enter the list"))
max=l[0]
for i in l:
    if max < i:
        max=i
print(max)


# most negative list "))
l=eval(input("enter"))
max=0
for i in l:
    if max > i:
        max=i
print(max)


# linear searching 
# array exist in two format sort or unsorted
# we can iterate over a array thorugh left to right or vice versa


l=[5,-1,7,8,2,3]
# let say k=3 k is searched key 
for i in range(0,len(l)+1):
    if i==3:
        print(True)
# what if 1 lakh data ??
# print(sorted(l))
for i in sorted(l):
    if i==3:
        print(i)
    if i > 3:
        # print(False) 
        break


