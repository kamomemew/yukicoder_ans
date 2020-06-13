#!/usr/bin/python3
#!coding: utf-8
from itertools import product
N=int(input())
def mat2_mul(X, Y):
    Z = [ [0, 0], 
          [0, 0] ]
    for (i,j,k) in product(range(2),range(2),range(2)):
        Z[i][j] += X[i][k] * Y[k][j]%1000000007
    return Z

def mat2_pow(X, n):
    if n == 0:
        return [ [1, 0],
                 [0, 1] ]
    elif n % 2:
        return mat2_mul(X, mat2_pow(X, n-1))  
    else:
        half_pow = mat2_pow(X, n/2)
        return mat2_mul(half_pow, half_pow)

def fib(n):
    if n == 0:
        return 0
    else:
        F = [ [0, 1],
              [1, 1] ]
        return mat2_pow(F, n-1)[1][1]


print(fib(N)*fib(N+1)%1000000007)
exit()
