#!/usr/bin/python3
yen_1=0
yen_5=0
yen_25=0
yen_125=0
#6 1

yen_1_orig,yen_5_orig=map(int,input().split())
#yen_5_orig=int(input())
print(yen_1_orig,yen_5_orig)
# flow
def p5(n):
    return n%5,n//5

ofl=0
yen_1,of=p5(yen_1_orig)
yen_5,of=p5(yen_5_orig+of)
yen_25,of=p5(of)
yen_125,of=p5(of)
yen_625,of=p5(of)
print(yen_625,yen_125,yen_25,yen_5,yen_1)
