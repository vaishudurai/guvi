n=int(input())
k=input().split()
x=[]
for i in range(0,n):
  if(int(k[i])==i):
    x.append(b[i])
if(x==[]):
  print("-1")
else:
  x.sort()
  for j in range(0,len(x)):
    print(x[j],end=" ")
