#include<stdio.h>
int main()
{
    int n,c=0;
    printf("enter val of n");
    scanf("%d",&n);

    for(int i=n;i>=1;i=i-2)   //i defines number of star to be printed
    {
        for(int j=1;i>=j;j++)
        {
            printf("%d",j);
        }
        c++;               // counter for white spaces 
        printf("\n");
        for(int k=1;k<=c;k++)
        {
            printf(" ");
        }
    }
    return 0;
}