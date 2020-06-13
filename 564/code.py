H,N=map(int,input().split())
L_H=[]
for i in range(N-1):
    L_H.append(int(input()))

L_H.sort(reverse=True)
postfix=["th","st","nd","rd","th","th","th","th","th","th","th"]
flag=True
for i in range(len(L_H)):
    if L_H[i] < H:
        flag=False
        break

if flag==True:
    i=i+2
else:
    i=i+1
p=postfix[int(str(i)[-1])]
print(str(i)+p)
