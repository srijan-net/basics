#include<stdio.h>
int main()
{
    int n;
    int arr1[n];
    printf("enter number of elements");
    scanf("%d",&n);
    // inputting elements using for loop 
    
    for(int i=0;i<n;i++)    //here i=0 for index value i.e-->{0,,,,n-1}
    {
       
       arr1[i]=i+2;
       
       
       
       
        // for(int j=1;j<=n;j++)
        // arr1[i]=j;               

        // scanf("%d",&arr1[i]);         // for filling array from user




    }
    for (int j = 0; j < n; j++)
    {
        printf("%d",arr1[j]);
    }
    



return 0;
}