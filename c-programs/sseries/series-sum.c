#include<stdio.h>
#include<math.h>
#include<stdbool.h>
int main()
{
    int inp;
    while(true)
    {
        printf("Menu driven prog. for series sum ...\n");
        printf("1. for  1+(2^2)+(3^3)+....(n^n)  \n");
        printf("2. for  1+2!+3!+....n!  \n");
        printf("3. for  1+1/2!+1/3!+....1/n!  \n");
        printf("4. for  1+1/2!+1/3!+....1/n!  \n");
        printf("69. for exit . :)  <3 .  \n");
        scanf("%d",&inp);


        if(inp==1)
        {
            int sum=0,n;
            printf("enter the range => ");
            scanf("%d",&n);
            for(int i=1;i<=n;i++)
            {
                sum=sum+pow(i,i);

            }
            printf("sum of : 1+(2^2)+(3^3)+....(n^n) ==> %d",sum);
            
        }
        
        if(inp==2)
        {
            int c,temp,sum=0,n;
            printf("enter the range => ");
            scanf("%d",&n);
            for(int i=1;i<=n;i++)
            {
                c=i;
                temp=1;
                while(temp!=c)
                {
                    temp=temp*c;
                    c=c-1;
                }
                sum=sum+temp;


            }

        }

    }
    return 0;
}