#include<stdio.h>
int main()
{
    int a,b,c;
    printf("\nenter sides of triangle\n");
    scanf("%d%d%d",a,b,c);
    if(a==b||b==c||c==a)
        printf("triangle is isoclese");
    else if(a==b&&b==c)
        printf("triangle is equi");
    else
        printf("triangle is scalen");
    printf("\nhellos");
    return 0;
}