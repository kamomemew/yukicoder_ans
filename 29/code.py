N=int(input())
L=[]
for i in range(N):
    L=L+list(map(int,input().split()))

p_up=0
rest=0
s=set(L)
for i in s:
    item_count = L.count(i)
    p_up = p_up + (item_count//2)
    rest = rest + item_count %2

p_up = p_up + rest//4
print(p_up)
