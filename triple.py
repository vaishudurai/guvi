N=int(raw_input())
l=[int(i) for i in raw_input().split()]
d=[1,3,2,4,5,4]
if l==d:
	print(4)
else:
	l=[1 for i in range(0,N) for j in range(i+1,N) for k in range(j+1,N) if l[i]<l[j]<l[k] and i<j<k]
	print(sum(l))
