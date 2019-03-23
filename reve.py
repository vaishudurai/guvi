line = raw_input()
a=line.split()
print(" ".join(i[::-1] for i in a ))
