A,B,C,D=map(int,input().split())
while True:
    if A <= int(D/(C+1)):
        if A*C <= B:
            print(A)
            exit()
    A=A-1 