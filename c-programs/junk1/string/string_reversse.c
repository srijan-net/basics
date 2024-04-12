#include<stdio.h>
#include<string.h>
void swap(char *,char *);
int main()
{
int i=0, l;
char str[50];
gets(str);
l=strlen(str)-1;
while(i<l)
{
    str[i]=str[l];
    i++;
    l=l-1;

}
puts(str);



    return 0;
}