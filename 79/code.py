a=[0,0,0,0,0,0]
input()
for i in list(map(int,input().split())):
    a[6-i]=a[6-i]+1
print(6-a.index(max(a)))
