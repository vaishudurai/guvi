def checkEven(N):
    if N%2==0:
        return "YES";
    else:
        return "NO";



if __name__ == "__main__":
    N,A,B=map(int, raw_input().split())
    if checkEven(N) == "NO":
        print("NO")
    else:
        par=N/2
        left=par%A
        if (left==0 or left%B==0):
            print("YES")
        else:
            print("NO")
