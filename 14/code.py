L=int(input())
input()
W=sorted(list(map(int,input().split())),reverse=True)
for i in range(len(W)):
    if L>=sum(W[i:]):
        print(len(W)-i)
        exit()
    
