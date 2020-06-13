dim_Y,dim_X=map(int,input().split())
_d=input()

OP=_d.split()[0]
X=_d.split()[1:]

for i in range(dim_Y):
    l=input()
    ll=""
    for j in range(dim_X):
        ll=ll+str(eval(X[j]+OP+l))+" "
    print(ll[:-1])
        
