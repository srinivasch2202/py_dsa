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


# l=[1,2,3,4]
# l.remove(1)
# print(l)

# while True:
#     if l==[]:
#         break
#     else:
#         l.pop()

l=eval(input("enter the list"))
max=l[0]
for i in l:
    if max < i:
        max=i
print(max)

