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
            for (int j=1; j<=i; j++)
            {
                if(j%2==0)
                    printf("1");
                else
                printf("0");
            }
            printf("\n");
        }
       if(i%2!=0)
            {
            for(int k=1;k<=i;k++)
            {
                if(k%2==0)
                    printf("0");
                else
                printf("1");
            }
            printf("\n");

        }

    }
return 0;
}