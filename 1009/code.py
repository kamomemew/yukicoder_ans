a,b=map(int,input().split())

def Integrate (a,b):
    return lambda x: x*(6*a*b - 3*a*x -3*b*x + 2*x*x)/6

F=Integrate(a,b)
print(F(a)-F(b))
    
