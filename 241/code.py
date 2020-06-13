#!/usr/bin/python3
import copy
N=int(input())
unfav=[]
ok=[]
for i in range(N):
    uf=int(input())
    unfav.append(uf)
    oklist=list(range(N))
    try:
        oklist.remove(uf)
    except ValueError:
        pass
    ok.append(oklist)

def regress(l,_n=None,num=None): # n はn人目、 numは確定番号
    LL=copy.deepcopy(l)
    if _n is None:
        for i in LL[0]:
            L=regress(LL,0,i)
            if L:
                return L
        if L is None:
            return None

    if num in LL[_n] and (LL[_n] is not None):
        LL[_n]=[num]
        for i in range(N):
            if i==_n:
                continue
            if num in LL[i]:
                LL[i].remove(num)
        if _n==N-1:
            return LL
    else:
        return None

    for j in LL[_n+1]:
        res=regress(LL,_n+1,j)
        if res:
            return res


ok_regress=regress(ok)
if ok_regress is None:
    print("-1")
else:
    for i in range(N):
        print(int(ok_regress[i][0]))
    
#print(ok_regress)
     