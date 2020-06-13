N=int(input())
points=list(map(int,input().split()))
between=[]
for i in range(len(points)-1):
    between.append(points[i+1]-points[i])
print(min(between))
print(points[-1]-points[0])
    



