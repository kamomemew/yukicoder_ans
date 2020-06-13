#!/usr/bin/python3
import sys
sys.setrecursionlimit(10000)

def op(x,y):
    if x==0 or y==0:
        print("Yes")
        exit()
    x_mul2=(x%2==0)
    y_mul2=(y%2==0)
    if (not x_mul2) and (not y_mul2):
        return
    elif x_mul2 and y_mul2:
        if (x//2)%2==1:
            op(x-1,y//2)
        elif(y//2)%2==1:
            op(x//2,y-1)
        else:
            op(x-1,y//2)
            op(x//2,y-1)
    elif x_mul2:
        op(x//2,y-1)
    else:
        op(x-1,y//2)
            
def op1(x,y):
    if x==0 and y==0:
        print("Yes")
        exit()
    if x%2==0 and y>0:
        x=x//2
        y=y-1
        op2(x,y)
        op1(x,y)

def op2(x,y):
    if x==0 and y==0:
        print("Yes")
        exit()
    if x>0 and y%2==0:
        x=x-1
        y=y//2
        op1(x//2,y-1)
        op2(x-1,y//2)


X,Y=map(int,input().split())
op(X,Y)
#op2(X,Y)
print("No")

