#!/usr/bin/python3
from math import gcd
import itertools
N_list= list(input())
gcd_total=None

for i in itertools.permutations(N_list):
    if not gcd_total:
        gcd_total = int("".join(i))
    elif gcd_total==1:
        print(1)
        exit()
    else:
        i=int("".join(i))
        gcd_total=gcd(i,gcd_total)
print(gcd_total)