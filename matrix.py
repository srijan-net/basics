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
        for i in matrix:
            print(i)
    row_read=int(input("enter the row no. to read -->"))
    col_read=int(input("enter col no to read -->"))
    print(matrix[row_read-1][col_read-1])
    #for row in matrix:            
    #    row_read-=1
    #    if row_read==count:
    #        print(row[col_read-1])

def matrix_edit():
    if matrix==[]:
        print("creating a matrix first")
        creat_matrix()    
    for i in matrix:
        print(i)
    row_edit=int(input("enter the row no.-->"))
    col_edit=int(input("enter col no -->"))
    val=int(input("enter val no -->"))
    matrix[row_edit-1][col_edit-1]=val
    for i in matrix:
        print(i)
    
while True:
    a=int(input("enter choice from the following:\n1.create a matrix\n2.read a matrix element\n3.eddit matrix\n4.to read matrix\n5.to stop\n===> "))
    if a==1:
        creat_matrix()
    if a==2:
        read_matrix_element()
    if a==3:
        matrix_edit()
    if a==4:
        if matrix==[]:
            print("creating a matrix first")
            creat_matrix()
        for i in matrix:
            print(i)
    if a==5:
        break