#!/usr/bin/python3
a=int(input())
islands=[[] for x in range(a)]
for i in range(a-1):
    m,n=map(int,input().split(" "))
    if m==1 or n ==1:
        print(i)
    if m>n:
        islands[n].append(m)
    else:
        islands[m].append(n)
for i in range(a-1):
    if len(islands[i])>2 or len(islands[i])==0:
        print("Alice")
        print(i)
        exit()
print("Bob")
