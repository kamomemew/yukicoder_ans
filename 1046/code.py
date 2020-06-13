N,K=map(int,input().split())
L=list(map(int,input().split()))
s=0
if sorted(L)[::-1][0] <0:
    print(sorted(L)[::-1][0])
    exit()
for i in sorted(L)[::-1][:K]:
    if i > 0:
        s=s+i
print(s)
