#!/usr/bin/python3
#!coding:utf-8
s=input()
comp="yukicoder"

for i in range(9):
    if s[i] != comp[i]:
        print(comp[i])
        exit()