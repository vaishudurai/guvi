o,k1=map(int,raw_input().split())
if o%10==0:
  o=str(o)
  c=0
  for i in range(len(o)-1,-1,-1):
    if o[i]=='0':
      c+=1
  if k1<=c:
    print(o)
  else:
    o=o[:-c]
    o=o+'0'*k1
    print(o)
elif 10%(o%10)==0:
  no=int('1'+'0'*k1)
  while True:
    if no%o==0:
      print(no)
      break
    else:
      no+=int('1'+'0'*k1)
else:
  print(str(n2)+k1*'0')
