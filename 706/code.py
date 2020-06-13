N=int(input())
count=[0 for x in range(1001)]
for i in range(N):
    e=input().count("^")
    count[e]=count[e]+1
print(1000-count[::-1].index(max(count)))
