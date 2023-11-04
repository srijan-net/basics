#include<stdio.h>
int main()
{
    int max,a,b,c,x;
    x=100;
    printf("enter three number\n ");
    scanf("%d%d%d",&a,&b,&c);
    // objective is to find greatest of three number 
    max=a>b?(a>c?a:5):(b>c?b:c);
   
    printf("%d",max);
    return 0;
}
