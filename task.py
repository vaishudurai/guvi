n=raw_input()
flag=0
for i in range(1,len(n)):
  j=0
  while j<len(n) and len(n[:j]+n[i+j:])==len(n)-i:
    o=n[:j]+n[j+i:]
    if int(o)%8==0:
      flag=1
      print('yes')
      break
    j+=1
  if flag==1:
      break
else:
  print('no')
