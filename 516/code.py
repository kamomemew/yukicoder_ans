L=[]
for i in range(3):
    L.append(input())
if L.count("RED")>L.count("BLUE"):
    print("RED")
else:
    print("BLUE")
