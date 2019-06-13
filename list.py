k=int(raw_input())
a=list(map(int,raw_input().split()))
for i in range(0,k-1):
  n=list(map(int,raw_input().split()))
  for j in n:
    if j not in a:
     a.append(j)
print(str(sorted(a)).strip('[]'))

