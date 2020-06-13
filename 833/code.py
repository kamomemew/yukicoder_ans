#!/usr/bin/python3
class train:
    def __init__ (self,c):
        self.connected=False
        self.cool=c
        self.setpoint=c
    def remodel(self):
        self.cool=self.cool+1
    def connect (self):
        self.connected=True
    def disconnect (self):
        self.connected=False


N,Q=input().split()
trains=[]
for t in input().split():
    trains.append(train(int(t)))

for i in range(int(Q)):
    q,x=input().split()
    x=int(x)
    if q=="1":
        trains[x-1].connect()
        trains[x].setpoint = trains[x-1].setpoint + trains[x-1].cool
    elif q=="2":
        trains[x-1].disconnect()
        trains[x-1].setpoint = trains[x-2].setpoint - trains[x-1].cool
    elif q=="3":
        trains[x-1].remodel()
    elif q=="4":
        while True:
            if not trains[x-1].connected:
                res = trains[x-1].setpoint
                break
            x=x+1
        print(res)
        

