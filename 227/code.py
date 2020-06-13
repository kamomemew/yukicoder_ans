cards=input().split()
card_dct={}
for c in cards:
    if c in card_dct.keys():
        card_dct[c]=card_dct[c]+1
    else:
        card_dct[c]=1

pair = list(card_dct.values())
if (3 in pair) and (2 in pair):
    print("FULL HOUSE")
    exit(0)
elif (pair.count(3)==1):
    print("THREE CARD")
    exit(0)
elif (pair.count(2)==2):
    print("TWO PAIR")
    exit(0)
elif (pair.count(2)==1):
    print("ONE PAIR")
    exit(0)
else:
    print("NO HAND")
    exit(0)