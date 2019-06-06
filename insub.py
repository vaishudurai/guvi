s1,s2=raw_input().split()
s=0
if len(s1)>len(s2):
    s1,s2=s2,s1
q=0
while q<len(s1):
    s+=(ord(s2[q])-ord(s1[q]))
    q+=1
for q in range(q,len(s2)):
    s+=ord(s2[q])-ord('a')+1
print(s)
