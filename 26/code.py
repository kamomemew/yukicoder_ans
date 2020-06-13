cups=[False,False,False,False]
N=int(input())
M=int(input())
cups[N]=True
for i in range(M):
    P,Q=map(int,input().split())
    cups[P],cups[Q]=cups[Q],cups[P]

for i in range(4):
    if cups[i]:
        print(i)
