import math
P,Q=map(int,input().split())
x=(P+Q)*10
def f (x):
    return (x**2 - (P+Q * x *math.log2(x)))

def df (x):
    return -1*((Q*math.log(x)+x*(-math.log(4))+Q)/math.log(2))
    
while True:
    prev=x
    x=x-((f(x))/df(x)) # ニュートン法
    if abs(prev - x) < 0.001:
        break
print(x)
