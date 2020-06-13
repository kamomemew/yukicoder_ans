#!/usr/bin/python3
i=int(input())
for _i in range(i):
    N=int(input())
    dev_8 =(N%8==0)
    dev_10 = (N%10==0)

    if dev_8 and dev_10:
        print("ikisugi")
    elif dev_8:
        print("iki")
    elif dev_10:
        print("sugi")
    else:
        print(N//3)