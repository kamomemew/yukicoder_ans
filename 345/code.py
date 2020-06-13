c_index=[]
s=input()
for i in range(len(s)):
    if s[i]=="c":
        c_index.append(i)
findW=False
m=1000
for i in c_index:
    findW=False
    for j in range(i,len(s)):
        if s[j]=="w":
            if findW == True:
                if m > (j+1-i):
                    m=(j+1-i)
                findW=False
                break
            else:
                findW=True
if m==1000:
    m=-1
print(m)
