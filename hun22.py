import numpy as np
new=int(raw_input())
l1=list(map(int,raw_input().split()))
rem=1
l=[]
for i in l1:
  rem=rem*i
for i in l1:
  l.append(rem//i)
myarray = np.asarray(l)
print(str(myarray).strip('[]'))
