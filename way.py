N=int(raw_input())
i=0
x=0
b=[]
while i<90 and i<N:
  r=0
  for j in str(N-i):
    r+=int(j)
  if r+(N-i)==N:
    x+=1
    b.append(N-i)
  i+=1
print(x)
for i in b:
  print(i)
