class board:
    def __init__(self):
        self.matrix = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    def isCanMove(self, turn, pos):
        if self.matrix[pos] == 0:
            return True
        return False

    def move(self, turn, pos):
        self.matrix[pos] = turn

    def undoMove(self, pos):
        self.matrix[pos] = 0

    def isEndGame(self):
        winState = [[0, 1, 2], [0, 3, 6], [2, 5, 8], [6, 7, 8], [0, 4, 8], [2, 4, 6], [1, 4, 7], [3, 4, 5]]
        score = [0, 1, -1]
        for i in range(0, 8):
            if self.matrix[winState[i][0]] != 0:
                if self.matrix[winState[i][0]] == self.matrix[winState[i][1]] and self.matrix[winState[i][0]] == \
                        self.matrix[winState[i][2]]:
                    return True, score[self.matrix[winState[i][0]]]
        for i in range(0, 9):
            if self.matrix[i] == 0:
                return False, 0
        return True, 0

    def generatedMove(self, turn):
        listMove = []
        for i in range(0, 9):
            if self.isCanMove(turn, i):
                listMove.append(i)
        return listMove


def AIMove(game):
    bestScore = 1
    listMove = game.generatedMove(2)
    bestMove = listMove[0]
    for i in listMove:
        game.move(2, i)
        score = Max(game, bestScore)
        game.undoMove(i)
        if score < bestScore:
            bestScore = score
            bestMove = i
    return bestMove


def Min(game, parentScore):
    rst, winLost = game.isEndGame()
    if rst:
        return winLost;
    bestScore = 1;
    listMove = game.generatedMove(2)
    for i in listMove:
        game.move(2, i)
        score = Max(game, bestScore)
        game.undoMove(i)
        if score < bestScore:
            bestScore = score
        if bestScore <= parentScore:
            return parentScore
    return bestScore


def Max(game, parentScore):
    rst, winLost = game.isEndGame()
    if rst:
        return winLost;
    bestScore = -1;
    listMove = game.generatedMove(1)
    for i in listMove:
        game.move(1, i)
        score = Min(game, bestScore)
        game.undoMove(i)
        if score > bestScore:
            bestScore = score
        if bestScore >= parentScore:
            return parentScore
    return bestScore


def printBoard(game):
    for i in range(0, 9):
        if game.matrix[i] == 0:
            print("-", end=' ')
        elif game.matrix[i] == 1:
            print("X", end=' ')
        else:
            print("O", end=' ')
        if i % 3 == 2:
            print()


game = board()
print("This is my tic tac toe board game in Python: ")
print("The state of game now: ")
printBoard(game)
rst, winLost = game.isEndGame()
while not rst:
    move = int(input("Press a number from 1 to 9 to make a move: ")) - 1
    if move >= 1 and move <= 9 and game.isCanMove(1, move):
        game.move(1, move)
        print("You pressed " + str(move + 1) + ", now the new state is: ")
        printBoard(game)
        rst, winLost = game.isEndGame()
        if rst:
            break
        move2 = AIMove(game)
        game.move(2, move2)
        print("The computer chooses the move " + str(move2 + 1) + ", now the new state is: ")
        printBoard(game)
    else:
        print("Your press is not vaild, let try again!")
    rst, winLost = game.isEndGame()

if winLost == 1:
    print("Congratulation, you won!")
elif winLost == -1:
    print("The compute won")
else:
    print("The match is draw.")
