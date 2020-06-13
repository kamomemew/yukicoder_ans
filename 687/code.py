#coding:utf-8
import random
N=int(input())
while True:
    a1=random.randint(1,10)
    a2=N-a1
    if (0<a1<11) and (0<a2<11):
        break
print(str(a1)+" "+str(a2))