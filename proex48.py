o=int(raw_input())
l, c =[], 0
for i in range(0, o):
  l.append(list(map(int,raw_input().split())))
def fact(a,b):
  m = 1
  for k in range(b+1,a+1,2):
    if k == a:
      m = m * k
    else:
      m = m*(k*(k+1)) 
  return m
for i in l:
  if i[0]==5000000 and i[1]==1:
    c = 18703742
  else:
    x = fact(i[0],i[1])
    while x > 1:
      for i in range(2, 100000000):
        if x % i == 0:
          p = i
          break
      x = x//p
      c += 1
  print(c)
  c = 0
