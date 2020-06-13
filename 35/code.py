N=int(input())
suc=0
mis=0
for i in range(N):
    #750 yukicoder
    _s=input().split()
    x,s=int(_s[0]),len(_s[1])
    w=min(12*x//1000,s)
    suc=suc+w
    mis=mis+(s-w)
print(suc,mis)
