i=input().split()
W,H,C=int(i[0]),int(i[1]),i[2]

e="".join([ "B" if x%2==1 else "W" for x in range(W) ])
o="".join([ "W" if x%2==1 else "B" for x in range(W) ])
if C=="W":
    print(e)
    even=True
else:
    print(o)
    even=False

for j in range(H-1):
    if even:
        print(o)
    else:
        print(e)
    even=not even

    
