N=int(input())
L=[ str(x) for x in range(1,N+1)]
expl=[]
print("? "+str(N),flush=True)
print(" ".join(L),flush=True)
ans=True if input()=="1" else False
if ans!=True:
    print("! 0",flush=True)
    print("",flush=True)
    exit()

for i in range(N):
    print("? "+str(N-1),flush=True)
    print(" ".join(L[0:i]+L[i+1:]),flush=True)
    ans_str=input()
    ans=True if ans_str=="1" else False
    if ans!=True:
        expl.append(str(i+1))

print("! "+str(len(expl)),flush=True)
print(" ".join(expl),flush=True)
