#include<stdio.h>
#include<math.h>
#include<stdbool.h>
int main()
{
    int i=1,c=0,n;
    printf("enter the range ie till number ==> ");        
    scanf("%d",&n);
    while(true)
    {
        int temp,sum=0,r=0,x,m,c1=0;
        m=i;
        x=i;
        temp=i;
        while(m!=0)
        {
            m=m/10;
            c1++;
        }
        while(x!=0)
        {
            r=x%10;
            x=x/10;
            sum=sum+pow(r,c1);
        }
        i++;    
        if(sum==temp)
            printf("%d\n",temp);        
        c++;
        if(c==n)
            break;
    }    
    return 0;
}