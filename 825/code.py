#!/usr/bin/python3
A,B,C=map(int,input().split())
pair=[0,1,2,3,4,5,6,7,8,9,10]
have_coin=A+10*B
for p in pair:
    if p+(10-p)*10 > have_coin:
        continue
    if p <= C:
        #print("Foo")
        print(p+(10-p)*10 - have_coin)
        #exit()
print("Impossible")
