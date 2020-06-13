#!/usr/bin/python3
import itertools
N,K=map(int,input().split())
l=input().split()
mx=max(list(map(lambda x:int(x[0]),l)))
def sort_weight(_n):
    if len(_n)==2:
        return float(_n)
    if len(_n)==1:
        return float(_n)*10+mx+0.5
def sort_weight_rev(_n):
    if len(_n)==2:
        return float(_n)
    if len(_n)==1:
        return float(_n)*10+mx-0.5

l2=sorted(l, key=sort_weight,reverse=True)
l3=sorted(l, key=sort_weight_rev,reverse=True)

count=0
kouho=[]
for i in itertools.permutations(l2):
    appendkouho=int("".join(i))
    if not appendkouho in kouho:
        kouho.append(appendkouho)
    count=count+1
    if count>=10*K:
        break
count=0
for i in itertools.permutations(l3):
    appendkouho=int("".join(i))
    if not appendkouho in kouho:
        kouho.append(appendkouho)
    count=count+1
    if count>=10*K:
        break
kouho=sorted(kouho,reverse=True)
for i in range(K):
    print(kouho[i])