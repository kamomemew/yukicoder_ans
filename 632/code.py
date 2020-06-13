#[('?', '2', '3'), ('?', '3', '2'), ('2', '?', '3'), ('2', '3', '?'), ('3', '?', '2'), ('3', '2', '?')]
s=input()
x1=s.replace("?","1")
x4=s.replace("?","4")
x1=list(map(int,x1.split()))
x4=list(map(int,x4.split()))
a=""
if (not (x1[0] < x1[1]< x1[2])) and (not (x1[0] > x1[1]> x1[2])) :
    a=a+"1"
if (not (x4[0] < x4[1]< x4[2])) and (not(x4[0] > x4[1]> x4[2])) :
    a=a+"4"
print(a)
