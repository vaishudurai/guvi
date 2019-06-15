n=raw_input()
if n==n[::-1]:
    print("yes")
else:
    value=n.strip("0")
    
    if value==value[::-1]:
        print("yes")
    else:
        value=n.lstrip("0")
        
        if value==value[::-1]:
            print("yes")
        else:
            print("no")
