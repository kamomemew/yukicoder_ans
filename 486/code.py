s=input()
E,W = s.find("OOO"),s.find("XXX")
if E == W == -1:
    print("NA")
    exit()
E = float("inf") if E==-1 else E
W = float("inf") if W==-1 else W
if E>W:
    print("West")
else:
    print("East")
