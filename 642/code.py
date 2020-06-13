N=int(input())
z=N
c=0
while z!=1:
    if z%2 ==0:
        c=c+1
        z=z//2
    else:
        c=c+1
        z=z+1 
print(c)

