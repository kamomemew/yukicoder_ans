#coding:utf-8
N=int(input())
fracs=[]
for _i in range(N):
    _stdin = input().split()
    a,b= int(_stdin[0]),int(_stdin[1])
    fracs.append({"a":a,"b":b,"v":(a/b)})

sorted=sorted(fracs,key=lambda x:x["v"])
for frac in sorted[::-1]:
    print("{} {}".format(frac["a"],frac["b"]))