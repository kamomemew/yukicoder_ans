#!/usr/bin/python3
#!coding:utf-8

N=int(input())
X=list(map(int,input().split()))
X.sort()
dst=[]
for i in range(len(X)-1):
    d=X[i+1]-X[i]
    if not d==0:
        dst.append(d)
try:
    print(min(dst))
except ValueError:
    print(0)