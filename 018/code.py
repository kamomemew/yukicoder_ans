def enc(s,rot):
    rot = rot % 26
    # only accept A --> Z
    # ord("A")==65, ord("Z")==90
    if (ord(s) + rot) > 90:
        t = chr((ord(s) + rot)-91+65)
    else:
        t = chr((ord(s) + rot))
    return t


def dec(s,rot):
    rot = rot % 26
    # only accept A --> Z
    # ord("A")==65, ord("Z")==90
    if (ord(s) - rot) < 65:
        t = chr((ord(s) - rot)+91-65)
    else:
        t = chr((ord(s) - rot))
    return t

S=input()
dS=""
for i in range(len(S)):
    dS=dS+dec(S[i],i+1)
print(dS)