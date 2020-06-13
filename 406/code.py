#coding:utf-8
input()
kamos=list(map(int,input().split()))
kamos.sort()
#print(kamos)
dst=kamos[1]-kamos[0]
for i in range(1,len(kamos)):
    if (kamos[i] - kamos[i-1] != dst) or (kamos[i] - kamos[i-1]==0):
        print("NO")
        exit()
print("YES")