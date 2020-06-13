N,K=map(int,input().split())
if K>N or K<1:
    print(0)
    exit()
if N%2 ==0:
    print(N-2)
else:
    if N//2+1 ==K:
        print(N-1)
    else:
        print(N-2)
