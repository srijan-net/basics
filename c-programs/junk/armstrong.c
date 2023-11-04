#include<stdio.h>
#include<math.h>
int main()
{

    int x,m,n,c=0,sum=0,r=0;
    printf("enter the number");
    scanf("%d",&n);
    m=n;
    x=n;
    while(n!=0)
    {
        n=n/10;
        c++;
        // printf("n==> %d\nc===> %d\n",n,c);   
    }
    while(m!=0)
    {
        r=m%10;
        m=m/10;
        sum=sum+pow(r,c); 
        // printf("s==> %d\nr===> %d\n",sum,r);   
    }
    if(sum==x)
        printf("its armstrong");
    else
        printf("not armstrong");
    return 0;
}