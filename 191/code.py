#!/usr/bin/python3
N=int(input())
C_all=[ int(x) for x in input().split()]
C_sum=sum(C_all)/10
r=0
for c in C_all:
    if c <= C_sum:
        r=r+30
print(r)
