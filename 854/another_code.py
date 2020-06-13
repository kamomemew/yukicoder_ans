#coding:utf-8
from functools import reduce
from operator import mul
input()
boxes=list(map(int,input().split()))
Q=int(input())
for i in range(Q):
    _in=list(map(int,input().split()))
    P,L,R = _in[0],_in[1],_in[2]
    if reduce(mul,boxes[L-1:R])%P==0:
        print("Yes")
    else:
        print("NO")