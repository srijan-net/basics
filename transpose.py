matrix=[[1,2],[3,1],[5,1]]
transpose=[]
row=len(matrix)         
for i in matrix:
    col=len(i)
    break
print(col)

def trans():
    if row==col:   
        c=0
        for x in range(row):
            row_t=[]
            for i in matrix:
                row_t.append(i[c])
            transpose.append(row_t)
            c+=1
        print(transpose)
    if col>row:
        d=col-row
        print(d)
        c=0
        for x in range(row+d):
            row_t=[]
            for i in matrix:
                row_t.append(i[c])
            transpose.append(row_t)
            c+=1
        print(transpose)
    if row>col:
        d=row-col
        c=0
        for x in range(row-d):
            row_t=[]
            for i in matrix:
                row_t.append(i[c])
            transpose.append(row_t)
            c+=1
        print(transpose)

trans()

