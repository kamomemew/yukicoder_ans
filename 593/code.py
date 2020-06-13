#!/usr/bin/python3
#!coding:utf-8

def tetra(b5):
    out = 0
    b5=str(b5)
    for i in range(1,len(str(b5))+1):
        out += int(b5[-i])*(4**(i-1))
    return out
for N4 in range(100):
    #N4=int(input())
    N10=tetra(N4)
    #print(N10)
    if N10%3==0 and N10%5==0:
        print("FizzBuzz")
    elif N10%3==0:
        print("Fizz")
    elif N10%5==0:
        print("Buzz")
    else:
        print(N4)