n=int(raw_input())
l=list(map(int,raw_input().split()))
m1=[]
a1=1
for i in range(n-1):
    if l[i]<l[i+1]:
        a1+=1
    else:
        m1.append(a1)
        a1=1
m1.append(a1)
print(max(m1))
