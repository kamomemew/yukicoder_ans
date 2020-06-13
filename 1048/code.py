#L R M K
N=0
L,R,M,K=map(int,input().split())
lst=sorted([i%M for i in list(range(L,R+1))])
if len(lst) > M:
    print("Yes")
    exit()

for i in range(len(lst)-1-M):
    if 0==sum(lst[0+i:M+i-1])%M:
        print("Yes")
        exit()
print("No")
exit()
