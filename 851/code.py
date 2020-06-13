#coding:utf-8
import itertools
N=int(input())
a=[]
s=[]
try:
    a.append(int(input()))
except ValueError:
    print('"assert"')
    exit(0)
for j in range(1,N):
    a.append(int(input()))
for i in itertools.combinations(a,2):
    if not i[0]+i[1] in s:
        s.append(i[0]+i[1])
s.sort()
print(s[-2])