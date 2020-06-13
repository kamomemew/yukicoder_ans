before=str(input())
N=int(input())
after=str(input())
if before.count("o") != after.count("o"):
    print("SUCCESS")
    exit()
if before.count("o") ==3 or before.count("x")==3:
    print("FAILURE")
    exit()
if N > 1:
    print("FAILURE")
    exit()
elif N == 0 and (before != after):
    print("SUCCESS")
    exit()
elif N==1 and (before == after) and (before == before[::-1]):
    print("SUCCESS")
    exit()
elif N==1 and (before != after) and (after == before[::-1]):
    print("SUCCESS")
    exit()
else:
    print("FAILURE")
