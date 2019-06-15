
n=int(raw_input())
l=list(map(int,raw_input().split()))
a_ha=0
b_ha=0
l.sort(reverse=True)
for i in l:
  s=a_ha+i
  if b_ha>s:
    a_ha=s
  else:
    a_ha=b_ha
    b_ha=s
print(a_ha,b_ha)
