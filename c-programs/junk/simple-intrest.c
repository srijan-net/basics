#include<stdio.h>
#include<math.h>
int main()
{
    float p,r,t,si;
    printf("enter principle amount ");
    scanf("%f",&p);
    printf("enter rate");
    scanf("%f",&r);
    printf("enter time in years ");
    scanf("%f",&t);
    si=(p*r*t)/100;
    printf("interst is %f \n",si);
}