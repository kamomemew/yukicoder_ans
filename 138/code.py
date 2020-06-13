#!/usr/bin/python3
#coding:utf-8
old=list(map(int,input().split(".")))
current=list(map(int,input().split(".")))
for i in range(3):
    if old[i]<current[i]:
        print("NO")
        exit(0)
    elif old[i]>current[i]:
        print("YES")
        exit(0)
    else:
        continue
print("YES")
