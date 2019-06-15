n,w=map(int,raw_input().split())
p=list(map(int,raw_input().split()))
v=list(map(int,raw_input().split()))
t=[]
c=0
for i in range(n):
    x=v[i]/p[i]
    t.append(x)
while w>=0 and len(t)>0:
    mindex=t.index(max(t))
    if w>=p[mindex]:
        c=c+v[mindex]
        w=w-p[mindex]
    p.pop(mindex)
    v.pop(mindex)
    t.pop(mindex)
print(c)
