n,p,q,r=map(int,raw_input().split())
l=list(map(int,raw_input().split()))
g=[]
for i in range(0,len(l)):
	for j in range(i,len(l)):
		for k in range(j,len(l)):
			g.append(p*l[i]+q*l[j]+r*l[k])
print(max(g))
