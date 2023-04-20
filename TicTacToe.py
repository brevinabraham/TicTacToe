import pandas as pd
class tictac:
    def __init__(self):
        self.board = pd.DataFrame([[0,0,0]]*3) 
        print(self.board) 
        self.player1 = 'x'
        self.player2 = 'o'
        self.start()

    def start(self):
        self.move1 = [input(str(self.player1) + " move: ")]
        self.update(self.player1, self.move1)
        self.wld(self.player1)

        self.move2 = [input(str(self.player2) + " move: ")]
        self.update(self.player2, self.move2)
        self.wld(self.player2)

        self.start()

    def update(self, player, move):        
        if self.board.loc[int(move[0][0]),int(move[0][1])] == 0:
            self.board.loc[int(move[0][0]),int(move[0][1])] = player
            print(self.board)
        else:
            move1 = [input(str(player) + " move: ")]
            self.update(player, move1)
    
    def wld(self,player):
        for i in range(3):#win by vertical
            if self.board.loc[:,i].equals(pd.Series([player]*3)):
                print(str(player) + " win")
                self.__init__()
        for row in self.board:#win by horizontal
            if self.board.loc[row,:].equals(pd.Series([player]*3)):
                print(str(player) + " win")
                self.__init__()
                
        if self.board.loc[0,0] == self.board.loc[1,1] == self.board.loc[2,2] == player or \
            self.board.loc[0,2] == self.board.loc[1,1] == self.board.loc[2,0] == player:#only other way is if diagonal 3inarow
            print(str(player)+ " win")
            self.__init__()

game = tictac()
game.__init__()