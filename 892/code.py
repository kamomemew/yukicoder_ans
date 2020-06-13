ab=list(map(int,input().split()))
op=False
for i in range(0,6,2):
    x=ab[i]
    p=ab[i+1]
    if (x%2 == 0) and (p != 0):
        op = op ^ False
    else:
        op = op ^ True
if op == False:
    print(":-)")
else:
    print(":-(")
    
