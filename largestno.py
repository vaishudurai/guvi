num1=input()
mylist = num1.split()
if (mylist[0] > mylist[1]) and (mylist[0] > mylist[2]):
   large=mylist[0]
elif (mylist[1] >mylist[0] ) and (mylist[1] > mylist[2]):   
   large=mylist[1]
else :
   large=mylist[2]
print (large)   
