#!/usr/bin/python3
R=input()
G=input()
B=input()
if R != "NONE":
    R_enable=16-len(R.split(","))
else:
    R_enable=16
if G != "NONE":
    G_enable=16-len(G.split(","))
else:
    G_enable=16
if B != "NONE":
    B_enable=16-len(B.split(","))
else:
    B_enable=16
print(R_enable**2*G_enable**2*B_enable**2)
