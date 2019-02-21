#include <stdio.h>
#include<string.h>
int main(void) {
	char s[10],temp;
	int i,l;
	scanf("%s",s);
	l=strlen(s);
	if(l%2==0)
	{
	for(i=0;i<l;i+=2)
             {
             temp=s[i];
             s[i]=s[i+1];
             s[i+1]=temp;
             }
   	 printf("%s",s);
	}
    else
    {
    for(i=0;i<l;i+=3)
             {
             temp=s[i];
             s[i]=s[i+1];
             s[i+1]=temp;
             }
   	 printf("%s",s);
	}
	return 0;
}
