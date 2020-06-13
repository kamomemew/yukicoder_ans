D,Q=map(int,input().split())
if Q<D:
    print(0)
    exit(0)
elif D==Q:
    print(4)
    exit(0)
elif  D < Q < D*2:
    print(8)
    exit(0)
elif D*2 == Q:
    print(4)
    exit(0)
else:
    print(0)
