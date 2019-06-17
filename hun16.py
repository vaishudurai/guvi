import numpy as np
p,s=map(int,raw_input().split())
m=[[abs(i-s),i]for i in [int(x) for x in raw_input().split()]]
m.sort()
m=m[1:]
m=[i[1] for i in m[:3]]
myarray = np.asarray(m)
print(str(myarray).strip('[]'))

