#include<stdio.h>
int main()
{
    int a,n;
    scanf("%d",&n);
    for(int i=1;i<=n;i++)
    {
        printf("factorial of each i is ==> ");
        printf("\n%d",fact(i));
 
    }
    return 0;
}



















int fact(int a)
{
    int factorial=1;
    for(int j=1;j<=a;j++)
    {
        factorial=factorial*j;
    }
    return factorial;
}
