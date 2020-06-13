import math
from functools import reduce
def gcd_list(numbers):
    return reduce(math.gcd, numbers)

N=int(input())
A=[]
for i in range(N):
    A.append(int(input()))
print(int(100/gcd_list(A)))