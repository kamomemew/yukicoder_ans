N=int(input())
k  = [0 for x in range(1000003)] 
kk = [0 for x in range(1000003)]
p  = [0 for x in range(1000003)]
k[0:3]  = [1,0,1]
kk[0:3] = [0,1,0]
p[0:3]  = [0,1,1]

for i in range(1,N):
    p[i]=(k[i-1]+kk[i-1])%(10**9+7)
    k[i+1]=p[i]%(10**9+7)
    kk[i+2]=p[i]%(10**9+7)

print((k[N-1]+kk[N-1]+p[N-1])%(10**9+7))

