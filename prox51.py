import numpy as np
o=int(raw_input())
l=list(map(int,raw_input().split()))
c=1
t=[]
for i in range(o):#loopstarts
    for j in range(i,o-1):
        if (l[j]>0 and l[j+1]<0) or (l[j]<0 and l[j+1]>0):
            c+=1
        else:
            break
    t.append(c)
            
    c=1
myarray = np.asarray(t)
print(str(myarray).strip('[]'))
