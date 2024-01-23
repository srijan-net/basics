#include<stdio.h>
int main()
{
    int n;
    printf("enter n row ===> ");
    scanf("%d",&n);
    
    
    for (int i=1;i<=n;i++)
    {
        if(i%2==0)
        {
            for (int j=65; j<=65+i-1; j++)
                printf("%c",j);
            printf("\n");
        }
       if(i%2!=0)
        {
            for(int k=1;k<=i;k++)
                printf("%d",k);
                printf("\n");


        }

    }
return 0;
}