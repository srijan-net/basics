#include<stdio.h>
int main()
{
    int b,p,val,c;
    printf("enter base ->");
    scanf("%d",&b);
    printf("enter power->");
    scanf("%d",&p);
    c=0;
    val=1;
    while(c!=p)
    {
      val=val*b;
        c++;
    }    
    printf("ans = %d",val);
    return 0;
}