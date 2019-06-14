n,m=map(int,raw_input().split())
v=list(map(int,raw_input().split()))
s=0
y=sorted(v)
x=(y[::-1])
for i in range(0,len(x)):
    z = m //(x[i])
    s = s + z
    m = m - (z *x[i])
print(s)
