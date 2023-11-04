#include<stdio.h>
#include<stdbool.h>
int main()
{
    int n,final,counter;
    printf("enter number till multiple of 3 required ");           //printing divisible of three .... 
    scanf("%d",&n);
    final=n/3;
    counter=1;
    while (true){
        if(counter<+final){
            printf("\n%d",counter*3);
            counter+=1;
        }
        else
            break;
    }
    return 0;

}