X,Y=raw_input().split()
a=abs(len(X)-len(Y))
for i in range(len(X)):
	if len(Y)==1 and m[i] in X:
		break
	if i>=len(X) or i>=len(Y):
		break
	if X[i]!=Y[i] and Y[i]:
		a=a+1
print(a)
