
S1,T=input().split()

dial_list=["I","II","III","IIII","V","VI","VII","VIII","IX","X","XI","XII"]
for i in range(len(dial_list)):
    if dial_list[i] == S1:
        break
i=i+1
T = int(T)%12 if int(T)>0 else abs(int(T))%12 *-1
if T+i > 12:
    a=T+i-12
elif T+i < 1:
    a=T+i+12
else:
    a=T+i
print(dial_list[a-1])    
