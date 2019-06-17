n,m=map(int,raw_input().split())
l=[]
for i in range(m):
  l.append(list(map(int,raw_input().split())))
cost=10000000
f=0
for i in range(m):
  if l[i][0]==1:
    s=l[i][1]
    c=l[i][2]
    for j in range(i+1,m):
      if l[j][0]==s:
        s=l[j][1]
        c+=l[j][2]
    if c<cost and s==n:
      cost=c
      f+=1
if f==0:
  print(-1)
else:
  print(cost)
