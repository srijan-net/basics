#include<stdio.h>
int main()
{

    float a,b ,c,i;
    int n;
    printf("enter the range==> ");
    scanf("%d",&n);
    a=0;
    b=1;
    c=1;
    printf("%.1f\n%.1f\n",a,b);
    for(i=0;i<n;i++)
    {

        c=a+b;
        printf("%.1f\n",c);
        a=b;
        b=c;


    }



    return 0;
}