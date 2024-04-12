#include<stdio.h>
#include<string.h>
int main()
{
    char str[1000];
// input string
    printf("enter string--> ");
    gets(str);

// Replace vowels with 'X'
    for (int i=0;i<strlen(str);i++) 
    {
       char c=str[i];
        if (c=='a'||c=='e'||c=='i'||c=='o'||c=='u') 
            str[i] = 'X';
    }
    for(int i=0;i<strlen(str);i++)
        printf("%c",str[i]);
    return 0;
}