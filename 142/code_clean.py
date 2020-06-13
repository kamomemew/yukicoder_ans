#!/usr/bin/python3
#!coding:utf-8
import numpy as np
stdin=input().split()
N,S,X,Y,Z=map(int,stdin)

def mk_list(N,S,X,Y,Z):
    l=[S]
    prev=S
    for _i in range(N-1):
        prev = (X * prev + Y) % Z
        l.append(prev)
    return l


def mk_list_bool(N,S,X,Y,Z):
    l=[S]
    prev=S
    for _i in range(N-1):
        prev = (X * prev + Y) % Z
        l.append(prev)
    ll=[ True if x%2==1 else False for x in l ]
    return ll


arr = np.array(mk_list_bool(N,S,X,Y,Z))


def mk_maskd_list(l,i,j,m,n):
    # l[i,j] --(copy)--> ll[m,n]
    ll = [False for _i in range(len(l))]
    ll[m-1:n-1] = l[i-1:j-1]
    for po in range(m-1,n):
        l[po]=l[po] ^ ll[po]
    return l



Q=int(input())
for _j in range(Q):
    I,J,K,L=map(int,input().split())
    arr = mk_maskd_list(arr,I,J,K,L)
for _i in list(arr):
    print("E" if _i==False else "O",end="")
print()