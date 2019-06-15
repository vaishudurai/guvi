n,d=map(int,raw_input().split())
l=list(map(int,raw_input().split()))
if d==1:
    print(min(l))
elif d==2:
    print(max(l[0],l[n-1]))
else:
    print(max(l))
