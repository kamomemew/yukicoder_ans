#!/usr/bin/python3
dummy=input()
prob_list=[int(x) for x in input().split ]
N=int(input())
dct={}
for _m in range(N):
    Q1,Q2=input().split()
    if Q2=="?":
        dct.