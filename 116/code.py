def is_kdmatsu(x,y,z):
    if not ((x != y) and (y != z) and (z != x)):
        return 0
    if x < y < z:
        return 0
    if z < y < x:
        return 0
    return 1

input()
L=list(map(int,input().split()))
count=0
for i in range(0,len(L)-2):
    count= count + is_kdmatsu(L[i],L[i+1],L[i+2])
print(count)

