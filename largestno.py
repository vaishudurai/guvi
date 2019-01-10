num1=input()
num2=input()
num3=input()
if (num1 > num2) and (num1 > num3):
   large=num1
if (num2 > num1) and (num2 > num3):   
   large=num2
if (num3>num1) and (num3>num2):
   large=num3
print (large)   
