from getTokens import get_tokens,distribute_tokens

class Handler():
    def __init__(self,playerList,dominoType = 7 ,initPlayer = 0):
        self.board = []
        self.type = dominoType
        self.playerList = playerList
        self.initPlayer = initPlayer
        self.sameBoard = 0
    
    def assingTokens(self):
        randomList = distribute_tokens(players=len(self.playerList), domino_type=self.type)
        
        i = 1
        j = 0
        while(i < len(randomList)):
            self.playerList[j].tokens = list(randomList[i])
            i += 1
            j += 1

    def getRandoms(self,tokensToAssing,amountTokens):
        pass
    
    def hasFinished(self):
        winnerList = []
        if(self.sameBoard == 4):
            playersPoints = []
            for i in range(len( self.playerList)):
                playersPoints.append((self.getPoints(self.playerList[i].tokens),i))
            
            playerPoints.sort()

            winnerPoints,winnerPlayer = playersPoints[0]
            winnerList.append(winnerPlayer)

            i = 1
            while( i < len(playersPoints)):
                points,player = playersPoints[i]
                if points == winnerPoints:
                    winnerList.append(player)
                else:
                    break
                i += 1
        
        else:
            for i in range(self.playerList):
                if(len(self.playerList[i].tokens) == 0):
                    winnerList.append(i)

        return winnerList

    def play(self):

        while(True):
            move = self.playerList[self.initPlayer].play(self.board)
            if(move == None):
                self.sameBoard += 1

            #verificar si la jugada es correcta

            move,pos = move    
            a,b = self.board[0]
            c,d = self.board.last()

            if(pos == 0):
                if(a == move[1]):
                    self.board.insert(0, move)
                elif(a == move[0]):
                    self.board.insert(0,move.reverse())
                else:
                    pass
                    #Jugada invalida

            else:
                if(d == move[0]):
                    self.board.append(move)
                elif(d == move[1]):
                    self.board.append(move.reverse())
                else:
                    pass
                    #Jugada invalida

            winnerList = self.hasFinished()
            if(len(winnerList)!= 0):
                return winnerList

    def simulate(self):
        pass
    

    def log(self):
        pass