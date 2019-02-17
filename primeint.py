l,r=map(int,raw_input().split())
c=0
for num in range(l,r+1):
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           c+=1
print(c)
