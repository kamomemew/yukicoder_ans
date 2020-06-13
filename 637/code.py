
def fiz_len(s):
    s=int(s)
    if s%15 ==0:
        return 8
    elif s%3==0 or s%5==0:
        return 4
    else:
        return len(str(s))
print(sum(list(map(fiz_len,input().split()))))