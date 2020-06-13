n=int(input())
s=input()
t=input()
Z=0
for i in range(len(s)):
    if s[i]!=t[i]:
        Z=Z+1
print(Z)
