N=int(input())
steps=0
max_index=N
while N!=1:
    if N%2 == 0:
        N=N//2
    else:
        N=N*3+1
    if max_index < N:
        max_index = N
    steps=steps+1
print(steps)
print(max_index)
