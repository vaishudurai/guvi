import numpy as np
o1 = int(raw_input())
a = list(map(int,raw_input().split()))
c1,l1 = 0,[]
b1 = [x for x in range(1,o1+1)]
for i in a:
  if i in b1:
    b1.remove(i)
k = 0
for i in range(0,o1-1):
  p = a[i]
  for j in range(i+1,o1):
    if p == a[j]:
      if p < b1[k]:
        a[j] = b1[k]
        c1 += 1
      else:
        a[i] = b1[k]
        c1 += 1
      k += 1
print(c1)
myarray = np.asarray(a)
print(str(myarray).strip('[]'))

