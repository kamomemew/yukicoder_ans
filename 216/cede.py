input()
point_list  = list(map(int,input().split()))
solved_list = list(map(int,input().split()))
myPoint=0
othersPoint=[0 for x in range(101)] 
for p,s in zip(point_list,solved_list):
    if s == 0:
        myPoint = myPoint+p
    else:
        othersPoint[s] = othersPoint[s]+p
if myPoint>=max(othersPoint):
    print("YES")
else:
    print("NO")
