A=int(input())
B=int(input())
DL=abs(1-(A/5000)/(B/200000))
DQ=abs(1-(A/(5000**2) )/ (B/(200000**2)))
print(1 if DL < DQ else 2)
