#!coding:utf-8
ref=[chr(i) for i in range(65,65+26)]
ref.append("?")
N=int(input())
L=list(map(int,input().split()))
T=int(input())

Timing=[1]*N

kekka={}

for i in range(T):
    NP=input().split()
    Name=NP[0]
    Prob_No=ref.index(NP[1])
    if Prob_No==26:
        kekka_now=[]
        for k in kekka.keys():
            kekka_now.append([k,kekka[k]])
        kekka_now=sorted(kekka_now, key=lambda x:(x[1][0],x[1][2]), reverse=True)
        
        for i in range(0,len(kekka_now)):
            if kekka_now[i][0]==Name:
                print(i+1)
    else:
        Point=int(50*L[Prob_No]+50*L[Prob_No]/(0.8+0.2*Timing[Prob_No]))
        Timing[Prob_No]=Timing[Prob_No]+1
        if Name in kekka:
            kekka[Name][0]=kekka[Name][0]+Point
            kekka[Name][1][Prob_No]=Point
            kekka[Name][2]=T-i
        else:
            kekka[Name]=[0,[0]*N,0,0]
            kekka[Name][0]=Point
            kekka[Name][1][Prob_No]=Point
            kekka[Name][2]=T-i
        



