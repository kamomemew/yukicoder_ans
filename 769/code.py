class UNOSim:
    """ Class doc """
    
    def __init__ (self,N):
        """ Class initialiser """
        self.player_N  = N-1
        self.prev_card = ""
        self.magnifi   = 0
        self.rev       = False
        self.players   = [ 0 for x in range(N)]
        self.turn      = -1

    def drop(self,card):
        self.progress()
        
        if  self.prev_card == "skip":
            self.progress()
            self.prev_card=""

        elif self.prev_card == "drawtwo" and card != "drawtwo":
            self.players[self.turn] = self.players[self.turn] - 2 * self.magnifi
            self.prev_card=""
            self.magnifi = 0
            self.progress()
        
        elif self.prev_card == "drawfour" and card != "drawfour":
            self.players[self.turn] = self.players[self.turn] - 4 * self.magnifi
            self.prev_card=""
            self.magnifi = 0
            self.progress()
            
        if card == "number": # "number", "drawtwo", "drawfour", "skip", "reverse"
            self.players[self.turn] = self.players[self.turn] + 1
            
        elif card == "drawtwo" or card == "drawfour":
            self.prev_card = card
            self.magnifi = self.magnifi + 1
            self.players[self.turn] = self.players[self.turn] + 1

        elif card == "skip":
            self.prev_card = "skip"
            self.players[self.turn] = self.players[self.turn] + 1
        
        elif card == "reverse":
            self.rev = not self.rev
            self.players[self.turn] = self.players[self.turn] + 1

    def progress(self):
        if self.rev != True: # normal
            if self.player_N == self.turn:
                self.turn = 0
            else:
                self.turn = self.turn + 1
        else: # reversed
            if self.turn == 0:
                self.turn = self.player_N
            else:
                self.turn = self.turn - 1    
N,M=map(int,input().split())
a=UNOSim(N)
for i in range(M):
    a.drop(input())
print("{} {}".format(a.turn+1,a.players[a.turn]))
    
