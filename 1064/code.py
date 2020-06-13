# coding:utf-8
# 2*x^2 + (a-c)*x (b-d)
# D = (a-c)**2 - 4 * 2 *(b-d)
from math import sqrt as sq
from decimal import *
a,b,c,d=map(int,input().split())
D=(Decimal(a-c))**Decimal(2) - Decimal(4) * Decimal(2) *(Decimal(b-d))
if D < 0:
    print("No")
if D==0:
    print("Yes")

x1 = (Decimal(-1)*Decimal(a-c) +  Decimal(sq(D)))/Decimal(2*2)
x2 = (Decimal(-1)*Decimal(a-c) -  Decimal(sq(D)))/Decimal(2*2)
y1 = Decimal(x1**2 + a*x1 + b)
y2 = Decimal(x2**2 + a*x1 + b)

print((y1-y2)/(x1-x2))
