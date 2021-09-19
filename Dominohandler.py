

class Handler():
    def __init__(self,playerList,dominoType = 6 ,initPlayer = 0):
        self.board = []
        self.type = dominoType
        self.playerList = playerList
        self.6Tokens = [(0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),
                        (2,2),(2,3),(2,4),(2,5),(2,6),(3,3),(3,4),(3,5),(3,6),(4,4),(4,5),(4,6),(5,5),
                        (5,6),(6,6)]
        self.9Tokens = [(0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8),(0,9),(1,1),(1,2),(1,3),
                        (1,4),(1,5),(1,6),(1,7),(1,8),(1,9),(2,2),(2,3),(2,4),(2,5),(2,6),(2,7),(2,8),
                        (2,9),(3,3),(3,4),(3,5),(3,6),(3,7),(3,8),(3,9),(4,4),(4,5),(4,6),(4,7),(4,8),
                        (4,9),(5,5),(5,6),(5,7),(5,8),(5,9),(6,6),(6,7),(6,8),(6,9),(7,7),(7,8),(7,9),
                        (8,8),(8,9),(9,9)]
        
        self.initPlayer = initPlayer
        self.sameBoard = 0
    
    def getTokens(self):
        if(self.type = 6):
            self.getTokens(7,28,self.6Tokens)
        else:
            self.getTokens(10,55,self.9Tokens)
    
    def getTokens(self,tokensToAssing,amountTokens,tokens):
        randomList = getRandoms(tokensToAssing * len(self.playerList) , amountTokens)
        player = -1
        assingList = []
        for i in range(len(randomList)):
            if(i % 7 == 0):
                player +=  1
                if(len(assingList) > 0):
                    self.playerList[player].tokens = list(assingList)
                assingList = []
            
            assingList.append(tokens[randomList[i]])
    
    def getRandoms(self,tokensToAssing,amountTokens):
        pass
    
    def hasFinished(self):
        winnerList = []
        if(self.sameBoard == 4):
            playersPoints = []
            for i in range(len( self.playerList)):
                playersPoints.append((self.getPoints(self.playerList[i].tokens),i))
            
            sort(playerPoints)

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
            c,d = move

            if(pos == 0):
                if(a == c):
                    self.board.insert(0, (d,c))
                elif(a == d):
                    self.board.insert(0,move)
                else:
                    pass
                    #Jugada invalida

            else:
                if(b == c):
                    self.board.append(move)
                elif(b == d):
                    self.board.append((d,c))
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