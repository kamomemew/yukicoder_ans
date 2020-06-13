#coding:utf-8
def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

input()
boxes=list(map(int,input().split()))
b_p=[]
for b in boxes:
    dct={}
    lst_prime=prime_factors(b)
    for l in lst_prime:
        l=str(l)
        if l in dct.keys():
            dct[l]=dct[l]+1
        else:
            dct[l]=1
    b_p.append(dct)
#print(b_p)
Q=int(input())

for i in range(Q):
    _in=list(map(int,input().split()))
    P,L,R = _in[0],_in[1],_in[2]
    dct_p={}
    lst_prime=prime_factors(P)
    res=True
    for l in lst_prime:
        l=str(l)
        if l in dct_p.keys():
            dct_p[l]=dct_p[l]+1
        else:
            dct_p[l]=1
    for k in dct_p.keys():
        if dct_p[k] > sum([ x[k] if k in x.keys() else 0 for x in b_p[L-1:R]]):
            print("NO")
            res=False
            break
    if res == True:
        print("Yes")