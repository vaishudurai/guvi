#include <stdio.h>
#include<string.h>
int main(void) {
	char a[10],b[10];
	scanf("%s %s",a,b);
	int p,q,i,j,r,t,w,x,y,z,f=0;
	m=strlen(a);
	n=strlen(b);
	if(p==q)
	{
	for(i=0;i<p;i++)
	{
		for(j=i+1;j<p;j++)
		{
			r=a[i];
			t=a[j];
			w=b[i];
			x=b[j];
			y=r-t;
			z=w-x;
			if(y==z)
			{
				f=1;
			}
			else
			{
				f=0;
				break;
			}
		}
	}
	}
	else
	{
		printf("no");
	}
	if(f==1)
	{
		printf("yes");
	}
	else
	{
		printf("no");
	}
	return 0;
}
