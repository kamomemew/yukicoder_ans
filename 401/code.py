#!/usr/bin/python3
#!coding:utf-8
N=int(input())
l=[]
zero_N=[]
for i in range(N):
    zero_N.append(0)
for i in range(N):
    l.append(zero_N)

m=0
n=0
mode = "→"
fill_num_list = [ i for i in range(1,N+1) ] [::-1]
while True:
    try:
        i = fill_num_list.pop()
    except IndexError:
        break
    
    if mode == "→":
        try:
            l[m][n]
        except IndexError:
            n=n-1
            mode="↓"
        if (l[m][n]==0):
            l[m][n]=i
            n=n+1
        else:
            mode="↓"

    if mode == "↓":
        try:
            l[m][n]
        except IndexError:
            n=n-1
            mode="↓"
        if (l[m][n]==0):
            l[m][n]=i
            n=n+1
        else:
            mode="↓"

    if mode == "→":
        try:
            l[m][n]
        except IndexError:
            n=n-1
            mode="↓"
        if (l[m][n]==0):
            l[m][n]=i
            n=n+1
        else:
            mode="↓"