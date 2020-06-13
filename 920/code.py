R,B,W=map(int,input().split())
P=0
P=min(R,B)
R=R-P
B=B-P
if W > max(R,B):
    P=P+max(R,B)
    W=W-max(R,B)
    R=B=0
else:
    P=P+W
    W=0
if W>0:
    P=P+W//2
print(P)
