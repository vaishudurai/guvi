upper,lower=map(int,raw_input().split())
for num in range(upper + 1,lower):
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)
