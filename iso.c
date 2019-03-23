#include <stdio.h>
#include<string.h>
int main(void) {
	char a[100],b[100];
	scanf("%s %s",a,b);
	int m,n,i,j,u,v,w,x,y,z,f=0;
	m=strlen(a);
	n=strlen(b);
	if(m==n)
	{
	for(i=0;i<m;i++)
	{
		for(j=i+1;j<m;j++)
		{
			u=a[i];
			v=a[j];
			w=b[i];
			x=b[j];
			y=u-v;
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
