n=int(raw_input())
m=[]
b=bin(2**n-1)[2::]
l=len(b)
for i in range(0,2**n):
	s=bin(i)[2::]
	if len(s)<l:
		m.append([s.count("1"),(l-len(s))*"0"+s])
	else:
		m.append([s.count("1"),s])
m.sort()
for i in range(0,len(m)):
	print(m[i][1])
