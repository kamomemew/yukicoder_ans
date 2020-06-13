day=set([23,24,25])
A,B=map(int,input().split())
print(len(list(day-set(range(A,B+1)))))
