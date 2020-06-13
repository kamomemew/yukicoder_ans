p1,p2,N=int(input()),int(input()),int(input())
L=[]
for i in range(N):
    L.append(input())
s=0
for i in set(L):
    s=s+(p1+p2)*(L.count(i)-1)
print(s)
    
