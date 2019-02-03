N=int(input())
while N>0:
    reverse=0
    reminder=N%10
    reverse=(reverse*10)+reminder
    N=N//10
    print reverse
    
