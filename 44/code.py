N=int(input())
L1=[0 for x in range(52)]
L2=[0 for x in range(52)]
L1[0]=L2[0]=0
L1[1]=1
L2[2]=L1[2]=1
for i in range(3,N+1):
    L1[i]=L1[i-1]+L2[i-1]
    L2[i]=L1[i-2]+L2[i-2]
print(L1[N]+L2[N])
