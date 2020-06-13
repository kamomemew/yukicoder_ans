i=int(input())
x=1
def ds(n):
    return 2*n + 0.5
def s(n):
    return int(0.5*(n**2)+0.5*n)
while True:
    prev=x
    x=x-((s(x)-i)/ds(x)) # ニュートン法
    if abs(prev - x) < 0.1:
        break
x=int(x)
print(x)
while True:
    print(s(x),i)
    if s(x)==i:
        print("YES")
        print(x)
        exit()
    elif s(x)>i:
        print("NO")
        exit()
    else:
        x=x+1
