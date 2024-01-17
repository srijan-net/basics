#include<stdio.h>
int main()
{
    int n;
    int arr[n];
    printf("enter elel \n");
    scanf("%d",&n);
    n=5;
    for(int i=0;i<n;i++)
    {
        arr[i]=i;

    }
    for (int j = 0; j < n; j++)
    {
        printf("%d",arr[j]);
    }
    return 0;








}