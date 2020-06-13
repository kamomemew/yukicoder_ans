N=int(input())
possible = set([ x for x in  range(10)])
for i in range(N):
    L=input().split()
    A=set(map(int,L[:-1]))
    R=L[-1]
    if R=="YES":
        possible = possible & A
    else:
        possible = possible & (set([ x for x in  range(10)])-A)

print(list(possible)[0])
    
