#include<stdio.h>
#include<string.h>
void main()
{
	int i,j,k,n;
	char a[10],b[10];
	scanf("%s",&a);
	scanf("%s",&b);
	for(i=0;a[i]!='\0';i++)
	{
		if(a[i]==b[i])
		{
			printf("%c",a[i]);
		}
		else
		{
			break;
		}
	}
}
