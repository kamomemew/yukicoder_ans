s=input()
if s=="":
    print(1)
    exit()
s=s.replace("R","1").replace("L","0")
print(int("1"+s, 2))
