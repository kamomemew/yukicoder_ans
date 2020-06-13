N = 0
A,B=map(int,input().split())
N = A*N + B
for i in range(1,1000):
    if N==0:
        print(i)
        exit()
    N = A*N + B
print(-1)
