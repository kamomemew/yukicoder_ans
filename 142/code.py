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
#print(mk_list(N,S,X,Y,Z))
#print(mk_list_bool(N,S,X,Y,Z))

arr = np.array(mk_list_bool(N,S,X,Y,Z))
#int_arr = mk_list(N,S,X,Y,Z)

def mk_maskd_list(l,i,j,m,n):
    # l[i,j] --(copy)--> ll[m,n]
    ll = [False for _i in range(len(l))]
    ll[m-1:n-1] = l[i-1:j-1]
    for po in range(m-1,n):
        l[po]=l[po] ^ ll[po]
    return l

def mk_maskd_list_int(l,i,j,m,n):
    # l[i,j] --(copy)--> ll[m,n]
    ll = [0 for _i in range(len(l))]
    ll[m-1:n-1] = l[i-1:j-1]
    #print(ll)
    return ll

def bogo_xor(l,ll):
    new_list=[]
    for _i in range(len(l)):
        new_list.append(l[_i]+ll[_i])
    return new_list

Q=int(input())
for _j in range(Q):
    I,J,K,L=map(int,input().split())
    arr = mk_maskd_list(arr,I,J,K,L)
    #int_arr = bogo_xor(int_arr,mk_maskd_list_int(int_arr,I,J,K,L))
    #print(arr)
    #print(int_arr)
#print(arr)
for _i in list(arr):
    print("E" if _i==False else "O",end="")
print()