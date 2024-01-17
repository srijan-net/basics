#include<stdio.h>
int main()
{
    int n,white_space;
    printf("enter n==> ");
    scanf("%d",&n);
    for(int i=1;i<=n;i++)
    {
        white_space=2*(n-i);

        for(int j=1;j<=i;j++)
            printf("%d",j);

        for(int k=1;k<=white_space;k++)
            printf(" ");

        for(int l=i;l>0;l--)
            printf("%d",l);

        printf("\n");
    }

    return 0;
}