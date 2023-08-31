matrix=[]
row=0
col=0

def creat_matrix():
    global row
    global col
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
    

def print_matrix():
    if matrix==[]:
        print("creat a matrix first")
        creat_matrix()
    for i in matrix:
        print(i)

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

def det2(a):
    print_matrix()
    r1_1=0   #row 1 element 1
    r1_2=0   #row 1 element 2
    r2_1=0
    r2_2=0
    count=0
    for i in a:
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
    det=(r1_1*r2_2)-(r1_2*r2_1)
    return det

def det3():
    tmat=[]    #first row excluded     
    first_row=[]                                          
    c=0
    for i in matrix:
        c+=1
        if c==1:
            for j in i:
                first_row.append(j)
        if c!=1:                    #finding determinant using row 1 therfore excluding row 1 
            tmat.append(i)
    temp_matrix=tmat
    temp_matrix2=temp_matrix


    t1=[]                                             #t---> temp matrix
    for i in tmat:
        t1.append(i[1:3])
    val1=det2(t1)
    
    t3=[]
    for i in tmat:
        t3.append(i[0:2])
    val3=det2(t3)

    t2=[]
    for i in temp_matrix2:
        del i[1]
    t2=temp_matrix2
    val2=det2(t2)
    # print(first_row)
    det=(val1*first_row[0])+(val2*first_row[1])+(val3*first_row[2])
    print(det)

while True:
    a=int(input("enter choice from the following:\n1.create a matrix\n2.read a matrix element\n3.eddit matrix\n4.to read entire matrix\n5.to find determinant [only 2x2/3x3] \n6.to stop\n===> "))
    if a==1:
        creat_matrix()
    if a==2:
        read_matrix_element()
    if a==3:
        matrix_edit()
    if a==4:
        print_matrix()
    if a==5:
        print_matrix()
        print(row,col)
        if row==col:
            print("hui")
            if row==2:
                print(det2(matrix))
            if row==3:
                det3()
        else:
            print("bruhh")            
    if a==6:
        break
