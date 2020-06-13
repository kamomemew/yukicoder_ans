#!/usr/bin/python3
A,B,C,D=map(int,input().split())
print(((A%D)*(B%D)*(C%D))%D)