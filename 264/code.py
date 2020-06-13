N,K=map(int,input().split())
if N==K:
    print("Drew")
    exit()
#ぐー, ちょき, ぱーをそれぞれ 0, 1, 2
if (N-K==-1) or (N-K==2):
    print("Won")
else:
    print("Lost")
