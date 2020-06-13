usi=input()
if usi[0]!="1":
    print(-1)
    exit()
if usi[1:]=="":
    print(-1)
    exit()
if usi[1:].replace("3","") != "":
    print(-1)
    exit()
print(usi.count("3"))
