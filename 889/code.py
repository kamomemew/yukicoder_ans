N=int(input())
if N in [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71]:
    print("Sosu!")
    exit()
if N in [x**2 for x in range(2,9)]:
    print("Heihosu!")
    exit()
if N in [x**3 for x in range(2,9)]:
    print("Ripposu!")
    exit()
if N in [6,28]:
    print("Kanzensu!")
    exit()
print(N)
