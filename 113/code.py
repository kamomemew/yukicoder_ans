#coding:utf-8
"""
       N
       |
  W --   -- E 
       |
       S

"""
import math
Q=input()
X=0
Y=0
for i in  range(len(Q)):
    if Q[i]=="N":
        Y=Y+1
    elif Q[i]=="E":
        X=X+1
    elif Q[i]=="S":
        Y=Y-1
    elif Q[i]=="W":
        X=X-1
print(math.sqrt(X**2+Y**2))