#include <stdio.h>

int main(void)
{
	long int a,n,d,add=0;
	scanf("%ld %ld %ld",&n,&a,&d);
            add = (n * (2 * a + (n - 1)* d ))/ 2;
	printf("%ld",add);
	return 0;
}
