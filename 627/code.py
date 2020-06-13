T=int(input())
N_b=0
for i in range(T):
    N_a=int(input())
    if abs(N_b - N_a) != 1:
        print("F")
        exit()
    N_b = N_a
print("T")
    
    
