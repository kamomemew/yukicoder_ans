#!/usr/bin/python3
A=input()
B=input()
if (len(A)>=2 and A[0]=="0") or (len(B)>=2 and B[0]=="0"):
    print("NG")
    exit()
try:
    A=int(A)
    B=int(B)
except ValueError:
    print("NG")
    exit()
if not(0<=A<=12345) or not(0<=B<=12345):
    print("NG")
    exit()
print("OK")
