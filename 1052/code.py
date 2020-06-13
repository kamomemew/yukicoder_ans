N,k=map(int,input().split())
if N%2 == 0:
    if 2*k >= N:
        print(N//2)
        exit()
    else:
        print(k+1)
        exit()            
else:
    if k >= N-1:
        print(N)
        exit()
    else:
        print(k+1)
