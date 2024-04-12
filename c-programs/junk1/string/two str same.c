#include<stdio.h>
#include<string.h>
int len;
int main()
{
    char str1[1000],str2[1000];
// input string
    printf("enter string1--> ");
    gets(str1);
    printf("enter string2--> ");
    gets(str2);
    len=strlen(str1);
int n=0;
// comparing
    for (int i=0;str1[i]!='\0';i++) 
    {
        if(str1[i]==str2[i])
        n=n+1;
    }
    if(len==n)
        printf("equal");
    else
        printf("no eql");   
   return 0;
}