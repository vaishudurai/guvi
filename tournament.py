N=int(raw_input())
m=1000
for i in range(0,20):
    if pow(2,i)<=N:
        x = abs(pow(2, i) - N)
        if x < m: m = x
print(m)
