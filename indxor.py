N,Q=map(int,raw_input().split())
a=list(map(int,raw_input().split()))
c=0
for i in range(0,Q):
  U,V=map(int,raw_input().split())
  b=a[U-1:V]
  for j in b:
    c=c^j
  print(c)
  c=0
