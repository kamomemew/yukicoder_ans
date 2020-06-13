#coding:utf-8
N=int(input())
tr1=input().split()
tr2=input().split()
for i in range(N):
    if tr1[i] != tr2[i]:
        print(i+1)
        print(tr1[i])
        print(tr2[i])
        exit()