N=int(input())
p=None
for i in range(N):
    X,Y=map(int,input().split())
    if p==None:
        p=Y-X
    elif p!=Y-X:
        print(-1)
        exit()
    elif Y-X < 1:
        print(-1)
        exit()
print(p)
