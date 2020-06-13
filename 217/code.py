import random
N=range(1,30)

def chk(L,N):
    l=[[] for i in range(N)]
    for i in range(N**2):
        #print(l[0])
        l[i//N].append(L[i])
    
    # よこ
    for i in range(N):
        if sum(l[0]) == sum(l[i]):
            pass
        else:
            return False
        
        for j in range(N):
            if sum(map(lambda row: row[0], l)) == sum(map(lambda row: row[j], l)):
                pass
            else:
                return False
        return True

for N in range(3,30):
    L=list(range(1,N**2+1))
    while True:
        random.shuffle(L)
        if chk(L,N):
            print(L)
            break
        
    
