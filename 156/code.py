N,M=map(int,input().split())
L=sorted(list(map(int,input().split())))
emptty=0
s=0
for i in range(len(L)):
    if L[i]+s <= M:
        emptty=emptty+1
        s=s+L[i]
print(emptty)
