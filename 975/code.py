X,N,M=input().split()
Mx=input().split()
Mv=input().split()
if (X in Mx) and (X in Mv):
    print("MrMaxValu")
    exit()
elif X in Mx:
    print("MrMax")
    exit()
elif X in Mv:
    print("MaxValu")
    exit()
else:
    print("-1")
