matrix=[]
row=0
col=0
def print_matrix():
    if matrix==[]:
        print("creat a matrix first")
        creat_matrix()
    for i in matrix:
        print(i)
def creat_matrix():
    row_num=int(input("enter the no. of rows "))
    col_num=int(input("enter num of colnms"))
    row=row_num
    col=col_num
    for i in range(1,row_num+1):    
        rows=[]                                    # here row get resseted to ["empty"] as the 1 loop for the row complets
        for j in range(1,col_num+1):
            a=int(input("enter value for ==>"))
            rows.append(a)
        matrix.append(rows)                         #matrix is completed   

def read_matrix_element():
    print_matrix()
    row_read=int(input("enter the row no. to read -->"))
    col_read=int(input("enter col no to read -->"))
    print(matrix[row_read-1][col_read-1])
    #for row in matrix:            
    #    row_read-=1
    #    if row_read==count:
    #        print(row[col_read-1])

def matrix_edit():
    print_matrix()
    row_edit=int(input("enter the row no.-->"))
    col_edit=int(input("enter col no -->"))
    val=int(input("enter val no -->"))
    matrix[row_edit-1][col_edit-1]=val
    for i in matrix:
        print(i)
def det2():
    r1_1=0   #row 1 element 1
    r1_2=0   #row 1 element 2
    r2_1=0
    r2_2=0
    count=0
    for i in matrix:
        for j in i:
            count+=1
            if count==1:
                r1_1=j
            if count==2:
                r1_2=j
            if count==3:
                r2_1=j
            if count==4:
                r2_2=j
    # print(r1_1,r1_2,r2_1,r2_2)            #just to check :)
    determi=(r1_1*r2_2)-(r1_2*r2_1)
    print(determi)

def det():
    print_matrix()    
    if row==col:

    # else:
        print("matrix should be a 'square matrix' to find determinant ")
while True:
    a=int(input("enter choice from the following:\n1.create a matrix\n2.read a matrix element\n3.eddit matrix\n4.to read matrix\n5.to find determinant \n6.to stop\n===> "))
    if a==1:
        creat_matrix()
    if a==2:
        read_matrix_element()
    if a==3:
        matrix_edit()
    if a==4:
        print_matrix()
    if a==5:
        break
    if a==6:
        break
