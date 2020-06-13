#!/usr/bin/python3
#!coding:utf-8
N=int(input())
aisatsu_mat=[]
candidate=[]
for _i in range(N):
    aisatsu_mat.append(input().split())

for person,i in zip (list(zip(*aisatsu_mat)), range(N)):
    #print(person,i)
    nyan=0
    for j in range (N):
        if j==i:
            continue
        if person[j] != "nyanpass":
            break
        else:
            nyan = nyan+1
    if nyan==N-1:
        candidate.append(i+1)

if candidate==[] or len(candidate)>1:
    print("-1")
else:
    print(candidate[0])