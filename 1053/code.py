input()
A=list(map(int,input().split()))

index=set()
gapped=[]
prev=-1
for i in range(len(A)):
    if prev !=A[i]:
        if A[i] in index:
            gapped.append(A[i])
        else:
            index.add(A[i])
    prev=A[i]
if len(gapped)>1:
    print(-1)
elif A[0] != A[-1] and len(gapped)>0:
    print(-1)
elif len(gapped)==0:
    print(0)
elif A[0] == A[-1] and len(gapped)==1:
    print(1)
else:
    print(-1)
