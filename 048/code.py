X=int(input())
Y=int(input())
L=int(input())

x_req=abs(X)//L if abs(X)%L==0 else abs(X)//L+1 
y_req=abs(Y)//L if abs(Y)%L==0 else abs(Y)//L+1
turn_req = 0 if abs(X)==0 and Y>=0 else 2 if Y<0 else 1
print(x_req,y_req,turn_req)s
print(x_req+y_req+turn_req) 