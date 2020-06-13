#!/usr/bin/python3
N=int(input())
cats=[]
for i in range(N):
    cats.append(int(input()))
nyan_count=0
for i in range(N):
    for j in range(i+1,N):
        if (cats[i]-i)-(cats[j]-j) >= j-i:
            nyan_count = nyan_count+1
print(nyan_count)
exit()
#port for C

