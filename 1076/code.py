N=float(input())
i=1
S=0
prev=0
while True:
    S=S+(N**i)
    if S-prev < 10**(-6):
        break
    else:
        prev=S
        i=i+1
print(S)
