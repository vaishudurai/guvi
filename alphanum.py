N=raw_input()
c=1
for i in range(len(N)-1):
    a=N[i]+N[i+1]
    b=int(a)
    if b<=26 and N[i]!="0":
        c+=1
if c==3:
    print(c)
else:
    print(c+(c-1)//2)
