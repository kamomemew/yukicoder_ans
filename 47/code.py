a=str(bin(int(input()))).replace("0b","")[::-1]
print(a)
b=0
for i in range(len(a)):
    b=b+int(a[i])*(i)
print(b)
