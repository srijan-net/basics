x=int(input("enter end position  "))
list=[0,1]
a=0
b=1
for i in range(2,x):
        c=a+b
        a=b
        b=c
        list.append(c)
list.sort(reverse=True)
print(len(list))
print(list)