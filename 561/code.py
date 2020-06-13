N,D=map(int,input().split())
_t,_k=map(int,input().split())
max_T,max_K = _t,_k - D
for i in range(N-1):
    _t,_k=map(int,input().split())
    max_T,max_K = max(max_K+(_t-D),max_T+_t),max(max_T+(_k-D),max_K+_k)
print(max(max_K,max_T))
