num=int(raw_input())
k1=list(map(int,raw_input().split()))
s1=[1]*num
for i in range(num):
    if i==0:
        if k1[i]>k1[i+1]:
            s1[i]=s1[i]+s1[i+1]
    elif i>0:
        if k1[i]>k1[i-1]:
            s1[i]=s1[i]+s1[i-1]
print(sum(s1))
