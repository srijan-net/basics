a=int(input("enter a number==>\n"))
list=[]
while True:
    dig=a%10
    a=a//10
    list.append(dig)
    if a//10==0:
        list.append(a)
        break
print(list)
digi=len(list)-1
revnum=0
for i in list:
    d1=i*(10**digi)          #here we are doing : revnum = 7000+500+60+1}example
    revnum+=d1               #here we are doing : revnum = 7000+500+60+1}example
    digi-=1
print(revnum)    
    




#num=input("enter number of times to enter element")
#print(num)    
#a=num[::-1]
#b=int(a)
#print(b,type(b))
