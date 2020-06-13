S,t,u=input().split()
t=int(t)
u=int(u)
if t>u: #tのほうが小さくなるように
    t,u=u,t
if t==u :
    print(S[0:t]+S[t+1:])
    exit()
else:
    print(S[0:t]+S[t+1:u]+S[u+1:])
