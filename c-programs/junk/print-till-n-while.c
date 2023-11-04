#include<stdio.h>
int main()
{
    int n,counter;
    printf("inpu the number\n");
    scanf("%d",&n);
    counter=3;
    while(counter<=n)
    {
        printf("\n%d",counter);
        counter+=3;

    }
    return 0;
}