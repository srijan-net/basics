matrix=[]

def creat_matrix():
    row_num=int(input("enter the no. of rows "))
    col_num=int(input("enter num of colnms"))
    for i in range(1,row_num+1):    
        rows=[]                                    # here row get resseted to ["empty"] as the 1 loop for the row complets
        for j in range(1,col_num+1):
            a=int(input("enter value for ==>"))
            rows.append(a)
        matrix.append(rows)                         #matrix is completed   

def read_matrix_element():
    if matrix==[]:
        print("creating a matrix first")
        creat_matrix()
    row_read=int(input("enter the row no.-->"))
    col_read=int(input("enter col no -->"))
    count=0
    for row in matrix:            
        count=count+1
        if row_read==count:
            print(row[col_read+1])

def matrix_edit():
    if matrix==[]:
        print("creating a matrix first")
        creat_matrix()    
    row_edit=int(input("enter the row no.-->"))
    col_edit=int(input("enter col no -->"))
    val=int(input("enter val no -->"))
    matrix[row_edit-1][col_edit-1]=val

creat_matrix()
for i in matrix:
    print(i)
    