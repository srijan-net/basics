matrix=[[1,4,6],[5,10,7],[4,3,8]]
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


def det3():
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
    
    


def det2(a):
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

det3()        


