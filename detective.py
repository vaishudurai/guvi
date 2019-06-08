N=int(raw_input())
l=list(map(int,raw_input().split()))
p=0
if(N==0):
    print("0")
else:
    for i in range(1,N):
        for j in range(0,i):
            if (l[j]<l[i]):
                p=p+l[j]
print(p)
