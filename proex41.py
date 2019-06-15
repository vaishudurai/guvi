n,m=raw_input().split()
n=int(n)
m=int(m)
s=''
u=2
if(n+m<=3):
    for i in range(0,n+m):
        if(i%2!=0):
            s=s+'0'
        else:
            s=s+'1'
else:    
    for i in range(0,n+m):
        if(i==u):
            s=s+'0'
            if(u==m):
                u=u+2
            else:
                u=u+3
        else:
            s=s+'1'
x=len(s)-1
if(int(s[x])==0):
    print('-1')
elif n==1 and m==2: print("011")
else:
    print(s)
