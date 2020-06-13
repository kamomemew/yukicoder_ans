l=sorted(list(map(int,input().split())))
if (l[3]-l[2]==1) and (l[2]-l[1]==1) and (l[1]-l[0]==1):
    print("Yes")
else:
    print("No")
