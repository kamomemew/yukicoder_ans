dct={}
dct["A"]=int(input())
dct["B"]=int(input())
dct["C"]=int(input())
dct=sorted(dct.items(), key=lambda x:x[1])
for i in range(3):
    print(dct.pop()[0])
