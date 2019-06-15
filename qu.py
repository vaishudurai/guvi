N=int(raw_input())
m=list(map(int,raw_input().split()))
m.sort()
s=0
c=0
for i in range(len(m)):
    if m[i]>=s:
        c=c+1
    s=s+m[i]
print(c)
