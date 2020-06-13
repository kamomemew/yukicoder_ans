N=int(input())
i=2
a=1
b=N
while i*i <= N:
    if b%(i**2)==0:
        b=b//(i**2)
        a=a*i
    else:
        i=i+1

print(a,b)
