A,B,C,D=map(int,input().split())
c=0
for i in range(A,B+1):
    for j in range(C,D+1):
        if i!=j:
            c=c+1
print(c)
        
