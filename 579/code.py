#!/usr/bin/python3
N=int(input())
n1=N*((N**2+6*N+5)%(10**9+7))
print(8*n1/3)