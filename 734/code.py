#!/usr/bin/python3
import math
A,B,C=map(int,input().split())
res=math.ceil((C*60*60)/(A*60-B))
if res<=0:
    print("-1")
else:
    print(res)