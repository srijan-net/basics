matrix=[[5,2],[3,1]]
row=len(matrix)         
for i in matrix:
    col=len(i)
    break
inv2x2=[]

def inverse():
    if row==col:
        if row==2:
            r1=[]
            r2=[]
            c=0
            for i in matrix:
                r2.append(i[c])
