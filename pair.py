n,k=map(int,raw_input().split())
m=list(map(int,raw_input().split()))
count=0
for i in range(len(m)):
  for j in range(i+1,len(m)):
    if(m[i]+m[j]==k):
        count=1
        break
if(count):
   print("yes")
else:
   print("no")    
