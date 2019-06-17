s=raw_input().split()
p=int(s[1])
s=raw_input().split()
s=[int(m) for m in s]
s.sort(reverse=1)
print(s[p-1])
