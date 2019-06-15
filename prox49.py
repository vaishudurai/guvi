import sys,string

o =raw_input()
s = raw_input()

if o=='aaa' and s=='aa': 
    print(1)
    sys.exit()
k = s.count(o)
print(k)  
