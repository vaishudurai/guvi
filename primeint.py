l,r=map(int,raw_input().split())
for num in range(l +1,r):
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)
