x,y,z=map(int,input().split())
N=z
if x <= z:
    N=N-1
if y <= z:
    N=N-1
if N<0:
    N=0
print(N)
