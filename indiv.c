#include<stdio.h>
int main()
{
    int n,p[10],i,j,k,count=0;
    scanf("%d",&n);
    for(i=0;i<n;i++)
    {
        scanf("%d",&p[i]);
    }
    for(i=0;i<n;i++)
    {
        for(j=0;j<n;j++)
        {
            if(p[i]==p[j])
            {
                count++;
            }
        }
        if(count==1)
        {
            printf("%d\t",p[i]);
        }
        count=0;
    }
    return 0;
}
