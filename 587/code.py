s=input()
dct={}
for i in range(len(s)):
    if s[i] in dct.keys():
        dct[s[i]] = dct[s[i]]+1
    else:
        dct[s[i]]=1
possible=None
for i  in dct.keys():
    if dct[i] == 2:
        pass
    elif dct[i] > 2:
        print("Impossible")
        exit()
    elif dct[i] < 1:
        print("Impossible")
        exit()
    elif (dct[i] == 1) and possible==None:
        possible=i
    elif (dct[i] == 1) and possible!=None:
        print("Impossible")
        exit()
print(possible)
