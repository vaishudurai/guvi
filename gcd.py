import math
import functools
N,K=map(int,raw_input().split())
l=[int(i) for i in raw_input().split()]
for i in range(K):
  a,b=map(int,raw_input().split())
  t=functools.reduce(math.gcd,l[a-1:b])
  print(t)
