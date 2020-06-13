import sys
input = sys.stdin.readline

N,Q=map(int,input().split())
A=list(map(int,input().split()))
Query=[list(map(int,input().split())) for i in range(Q)]

#Segment tree(1-indexed,再帰を使わないもの)

def seg_function(x,y):#Segment treeで扱うfunction
    return x+y

seg_el=1<<(N.bit_length())#Segment treeの台の要素数
SEG=[0]*(2*seg_el)#1-indexedなので、要素数2*seg_el.Segment treeの初期値で初期化

for i in range(N):#Aを対応する箇所へupdate
    SEG[i+seg_el]=A[i]

for i in range(seg_el-1,0,-1):#親の部分もupdate
    SEG[i]=seg_function(SEG[i*2],SEG[i*2+1])

def update(n,x,seg_el):#A[n]を+x更新（反映）
    i=n+seg_el
    SEG[i]+=x
    i>>=1#子ノードへ
    
    while i!=0:
        SEG[i]=seg_function(SEG[i*2],SEG[i*2+1])
        i>>=1
        
def getvalues(l,r):#区間[l,r)に関するseg_functionを調べる
    L=l+seg_el
    R=r+seg_el
    ANS=0

    while L<R:
        if L & 1:
            ANS=seg_function(ANS , SEG[L])
            L+=1

        if R & 1:
            R-=1
            ANS=seg_function(ANS , SEG[R])
        L>>=1
        R>>=1

    return ANS

LIST=[1]*N
BIT=[0]*(N+2)
BL=(N+2).bit_length()

def update_b(v,w):#vにwを加える
    while v<=N+1:
        BIT[v]+=w
        v+=(v&(-v))#たとえばv=3→v=4へ

def getvalue_b(v):#MIN～vの区間の和を求める
    ANS=0
    while v!=0:
        ANS+=BIT[v]
        v-=(v&(-v))#たとえばv=3→v=2へ
    return ANS

def lower_bound(x):
    w=0
    for i in range(BL-1,-1,-1):
        if w+(1<<i)<N+1 and BIT[w+(1<<i)]<x:
            x-=BIT[w+(1<<i)]
            w+=(1<<i)

    return w


for i in range(1,N+2):
    update_b(i,1)

for q,x in Query:
    if q==1:
        if LIST[x-1]==1:
            LIST[x-1]=0
            update_b(x+1,-1)

    elif q==2:
        if LIST[x-1]==0:
            LIST[x-1]=1
            update_b(x+1,1)

    elif q==3:
        update(x-1,1,seg_el)

    else:
        
        s=getvalue_b(x)
        #値がsの区間を調べる
        print(getvalues(lower_bound(s),lower_bound(s+1)))
