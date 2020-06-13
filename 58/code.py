#!/usr/bin/python3
#!coding:utf-8
import random
def dice():
    return [1,2,3,4,5,6][random.randint(0,5)]
def cheat():
    return [4,5,6,4,5,6][random.randint(0,5)]
N=int(input())
K=int(input())
win=0
lose=0
for i in range(1200003):
    m,n=0,0
    for j in range(N):
        m=m+dice()
    for k in range(N-K):
        n=n+dice()
    for l in range(K):
        n=n+cheat()
    if n>m:
        win=win+1
    else:
        lose=lose+1
print(win/1200003)
