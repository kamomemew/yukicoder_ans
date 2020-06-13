from decimal import *
i=Decimal(input())
x=1

def df(n):
    return 2*n + Decimal(0.5)

def f(n):
    return Decimal(0.5)*(n**2)+Decimal(0.5)*n-i
def s(n):
    return Decimal(0.5)*(n**2)+Decimal(0.5)*n
op=1
while True:
    prev=x
    x=x-(f(x)/df(x)) # ニュートン法
    if abs(prev - x) < 0.0001:
        break

x=Decimal(int(x-3))

for j in range(6):
    x=x+1
    if s(x)==i:
        print("YES")
        print(x)
        exit()
print("NO")
