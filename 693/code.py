N=int(input())
As=list(map(int,input().split()))
As.sort()
s=0
for i in range(len(As)):
    s=s+abs(As[i]-(i+1))
print(s)
    
