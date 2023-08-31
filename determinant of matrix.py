matrix=[[1,4],[5,10]]
row=0
col=0
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


def det2():
    r=0
    for i in matrix:
        for j in i:
            print(j)


def det3():
    print("limiting this to 2x2 and 3x3 matrix only!!")
    temp_matrix=[]
    # for i in matrix:
det2()