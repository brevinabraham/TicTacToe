import pandas as pd
#Sarah Is Fantastic 
class tictac:
    def __init__(self):
        self.board = pd.DataFrame([[0,0,0]]*3) #initialising the board
        print(self.board) 
        self.players = ['x','o']
        self.start()

    def start(self):
        for playr in self.players:
            self.move = [input(str(playr) + " move: ")]
            self.update(playr, self.move)
            self.wl(playr)

        self.start()

    def update(self, player, move):
        try:
            if self.board.loc[int(move[0][0]),int(move[0][1])] == 0:
                self.board.loc[int(move[0][0]),int(move[0][1])] = player
                print(self.board)
            else:
                move1 = [input(str(player) + " move: ")]
                self.update(player, move1)
        except:
            print("outside map")
            move1 = [input(str(player) + " move: ")]
            self.update(player, move1)


    def fullboard(self):
        if len(self.board.loc[(self.board.loc[:,0]==0) | (self.board.loc[:,1]==0) | (self.board.loc[:,2]==0)]) ==0:
            print("***draw***")
            tictac()

    def wl(self,player):
        for i in range(3):#win by vertical
            if self.board.loc[:,i].equals(pd.Series([player]*3)):
                print("***" + str(player) + " win***")
                tictac()
        for row in self.board:#win by horizontal
            if self.board.loc[row,:].equals(pd.Series([player]*3)):
                print("***" + str(player) + " win***")
                tictac()
                
        if self.board.loc[0,0] == self.board.loc[1,1] == self.board.loc[2,2] == player or \
            self.board.loc[0,2] == self.board.loc[1,1] == self.board.loc[2,0] == player:#only other way is if diagonal 3inarow
            print("***" + str(player) + " win***")
            tictac()
        self.fullboard()

game = tictac()
game()