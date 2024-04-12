#include<stdio.h>
int n,m;
int main()
{
    printf("enter n,m\n");
    scanf("%d",&n);
    scanf("%d",&m);
    int arr[n][m];
// input
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<m;j++)
        {
            scanf("%d",&arr[i][j]);
        }
    }
// output
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<m;j++)
        {
            printf("%d",arr[i][j]);
        }
        printf("\n");
    }


// check for uppr triangle
    if (check(arr)) {
        printf("The matrix is upper triangular.\n");
    } else {
        printf("The matrix is not upper triangular.\n");
    }
    
    return 0;
}
int check(int matrix[n][m])
    {
    int i, j;
    for (i=1;i<n;i++) 
    {
        for (j=0;j<i;j++) 
        {
            if (matrix[i][j] != 0) 
            {
                return 0; // Not upper triangular
            }
        }
    }
    return 1;           // Upper triangular
}