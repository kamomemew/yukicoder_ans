N,dummy=map(int,input().split())
c=0
for _n in range(N):
    c=c+input().count("W")
print(c)