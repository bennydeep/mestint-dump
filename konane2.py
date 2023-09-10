
"""Nem saját kód, csak egy githubos python2-es megoldás modernizálása,
    csak gondoltam ha Tanár Úrnak esetleg nem lenne működő python3 Konane megoldása, akkor legyen,
    így KELLETT volna megoldani, csak hát idő szűkében nem sikerült,
    na meg ilyen okos kódot nem is tudtam volna írni """

import random
import copy


class KonaneError(AttributeError):
    print("rip")

class Konane:
    def __init__(self, n):
        self.size = n
        self.reset()

    def reset(self):
        """
        reseteli a táblát
        """
        self.board = []
        value = 'B'
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append(value)
                value = self.opponent(value)
            self.board.append(row)
            if self.size%2 == 0:
                value = self.opponent(value)

    def __str__(self):
        return self.boardToStr(self.board)

    def boardToStr(self, board):
        """
        visszaadja stringként a konane táblát
        """
        result = "  "
        for i in range(self.size):
            result += str(i) + " "
        result += "\n"
        for i in range(self.size):
            result += str(i) + " "
            for j in range(self.size):
                result += str(board[i][j]) + " "
            result += "\n"
        return result

    def valid(self, row, col):
        """
        igazzal tér vissza ha a sor oszlop valid
        """
        return row >= 0 and col >= 0 and row < self.size and col < self.size

    def contains(self, board, row, col, symbol):
        """
        igazzal tér vissza ha a sor oszlop valid és tartalmazza az adott szimbólumot
        """
        return self.valid(row,col) and board[row][col]==symbol

    def countSymbol(self, board, symbol):
        """
        visszaadja hogy hány van az adott szimbólumból a táblán
        """
        count = 0
        for r in range(self.size):
            for c in range(self.size):
                if board[r][c] == symbol:
                    count += 1
        return count

    def opponent(self, player):
        """
        ad egy szimbólumot a játékosnak ,és az ellenfélnek meg az ellenkezőt
        """
        if player == 'B':
            return 'W'
        else:
            return 'B'

    def distance(self, r1, c1, r2, c2):
        """
        vertikálisan és horizontálisan visszaadja két pont távolságát
        """
        return abs(r1-r2 + c1-c2)

    def makeMove(self, player, move):
        """
        updateli a táblát az adott lépés alapján
        """
        self.board = self.nextBoard(self.board, player, move)

    def nextBoard(self, board, player, move):
        """
        a jelenlegi tábla egy másolatán létrehajta a lépést , KonaneError ha nem megfelelő a lépés
        a tábla másolatát adja vissza és nem módosítja az eredetit
        """

        if len(move) != 4:
            raise KonaneError
        r1 = int(move[0])
        c1 = int(move[1])
        r2 = int(move[2])
        c2 = int(move[3])
        next = copy.deepcopy(board)
        if not (self.valid(r1, c1) and self.valid(r2, c2)):
            raise KonaneError
        if next[r1][c1] != player:
            raise KonaneError
        dist = self.distance(r1, c1, r2, c2)
        if dist == 0:
            if self.openingMove(board):
                next[r1][c1] = "."
                return next
            raise KonaneError
        if next[r2][c2] != ".":
            raise KonaneError
        jumps = int(dist//2)
        dr = int((r2 - r1)/dist)
        dc = int((c2 - c1)/dist)
        for i in range(jumps):
            if next[r1+dr][c1+dc] != self.opponent(player):
                raise KonaneError
            next[r1][c1] = "."
            next[r1+dr][c1+dc] = "."
            r1 += 2*dr
            c1 += 2*dc
            next[r1][c1] = player
        return next

    def openingMove(self, board):
        """
        az alapján hogy mennyi üres hely van a táblán, visszaadja hogy kezdő lépés van, vagy már megy a játék
        """
        return self.countSymbol(board, ".") <= 1

    def generateFirstMoves(self, board):
        """
        megadja a lehetséges kezdőlépéseket
        """
        moves = []
        moves.append([0]*4)
        moves.append([self.size-1]*4)
        moves.append([self.size//2]*4)
        moves.append([(self.size//2)-1]*4)
        return moves

    def generateSecondMoves(self, board):
        """
        megadja a lehetséges másodlépéseket
        """
        moves = []
        if board[0][0] == ".":
            moves.append([0,1]*2)
            moves.append([1,0]*2)
            return moves
        elif board[self.size-1][self.size-1] == ".":
            moves.append([self.size-1,self.size-2]*2)
            moves.append([self.size-2,self.size-1]*2)
            return moves
        elif board[self.size//2-1][self.size//2-1] == ".":
            pos = self.size//2 -1
        else:
            pos = self.size//2
        moves.append([pos,pos-1]*2)
        moves.append([pos+1,pos]*2)
        moves.append([pos,pos+1]*2)
        moves.append([pos-1,pos]*2)
        return moves

    def check(self, board, r, c, rd, cd, factor, opponent):
        """
        ellenőrzi hogy lehetséges e az ugrás a kezdő pozi és az rd cd alapján
        a rekurzív használat miatt a lehetséges dupla ugrásokat is
        figyelembe veszi, visszaadja az összes lehetséges ugrást
        az adott irányba
        """
        if self.contains(board,r+factor*rd,c+factor*cd,opponent) and \
           self.contains(board,r+(factor+1)*rd,c+(factor+1)*cd,'.'):
            return [[r,c,r+(factor+1)*rd,c+(factor+1)*cd]] + \
                   self.check(board,r,c,rd,cd,factor+2,opponent)
        else:
            return []

    def generateMoves(self, board, player):
        """
        Visszaadja az adott játékosnak az összes lehetséges lépését a jelenlegi tábla alapján
        """
        if self.openingMove(board):
            if player=='B':
                return self.generateFirstMoves(board)
            else:
                return self.generateSecondMoves(board)
        else:
            moves = []
            rd = [-1,0,1,0]
            cd = [0,1,0,-1]
            for r in range(self.size):
                for c in range(self.size):
                    if board[r][c] == player:
                        for i in range(len(rd)):
                            moves += self.check(board,r,c,rd[i],cd[i],1,
                                                self.opponent(player))
            return moves

    def playOneGame(self, p1, p2, show):
        """
        meg lehet adni hogy kik között menjen a meccs, lehet ez ember vs ember
        ember vs random player, ember vs minimax player, minimax vs minimax, és stbstb
        visszatér a győztessel, a show igaz hamis értékével állítható hogy látszódjanak
        e a lépések, vagy sem
        """
        self.reset()
        p1.initialize('B')
        p2.initialize('W')
        if show:
            print (p1.name, "vs", p2.name)

        turn = 1
        while 1:
            if show:
                print (self)
                print ("player B's turn [", turn, "]")
            move = p1.getMove(self.board)
            if move == []:
                result = 'W'
                break
            try:
                self.makeMove('B', move)
            except KonaneError:
                print ("ERROR: invalid move by", p1.name)
                result = 'W'
                break
            turn += 1
            if show:
                print(move)
                print()
                print(self)
                print("player W's turn [", turn, "]")
            move = p2.getMove(self.board)
            if not move:
                result = 'B'
                break
            try:
                self.makeMove('W', move)
            except KonaneError:
                print ("ERROR: invalid move by", p2.name)
                result = 'B'
                break
            turn += 1
            if show:
                print (move)
                print()
        if show:
            print ("Game over")
        return result



class Player:
    pass
    #name = "Player"


class HumanPlayer(Player):
    """
    ember által irányított játékos
    """
    def initialize(self, side):
        self.side = side
        self.name = "Human"
    def getMove(self, board):
        inputs = list(map(int, input("Enter r1 c1 r2 c2 (or -1's to concede): ").split()))
        if inputs[1] == -1:
            return []
        return inputs

class RandomPlayer(Konane, Player):
    """
    "gép által irányított" játékos, ami a lehetséges lépések közül random választ
    """
    def initialize(self, side):
        self.side = side
        self.name = "RandomPlayer"
    def getMove(self, board):
        moves = self.generateMoves(board, self.side)
        n = len(moves)
        if n == 0:
            return []
        else:
            return moves[random.randrange(0, n)]

class MinimaxPlayer(Konane, Player):
    """
    "gép által irányított" játékos, ami a minmax algoritmust veszi alapul, ergo okosabb mint a random játékos
    """
    def __init__(self, size, depthLimit):
        Konane.__init__(self, size)
        self.limit = depthLimit

    def initialize(self, side):
        self.side = side
        self.name = "Mr. Roboto"

    def getMove(self, board):
        """
        visszaad egy lehetséges lépést
        """
        moves = self.generateMoves(board, self.side)

        if not moves:
            return []

        values = []
        alpha = -float("inf")
        for move in moves:
            values.append(self.minimax(self.nextBoard(board, self.side, move), 1, alpha, float("inf")))

            if max(values) > alpha:
                alpha = max(values)

        return moves[values.index(max(values))]

    def eval(self, board):
        """
        megadja a tábla heurisztikáit
        """
        return self.movablePieces(board, self.side) - (1.5 * self.movablePieces(board, self.opponent(self.side))) + (self.movesCount(board, self.side) - self.movesCount(board, self.opponent(self.side)))

    def movesCount(self, board, player):
        """
        megadja a lehetséges lépések heurisztikáit
        """
        return len(self.generateMoves(board, player))

    def movablePieces(self, board, player):
        """
        megadja a mozdítható elemek heurisztikáit
        """
        moves = self.generateMoves(board, player)
        counter = 0
        pieces = []
        for move in moves:
            if [moves[counter][0], moves[counter][1]] not in pieces:
                pieces.append([moves[counter][0], moves[counter][1]])
            counter += 1
        return len(pieces)

    def extendPath(self, board, side):
        """
        visszaadja az összes lehetséges lépést ,az adott tábla állapota és az adott játékos alapján
        """
        moves = self.generateMoves(board, side)
        boards = []
        for move in moves:
            boards.append(self.nextBoard(board, side, move))

        return boards

    def minimax(self, board, depth, alpha, beta):
        """
        minimax algoritmus használata, a mélységgel állítható hogy "mennyire lásson előre"
        """
        if depth >= self.limit:
            return self.eval(board)

        isMax = depth % 2 == 0

        if isMax:
            nextBoards = self.extendPath(board, self.side)
        else:
            nextBoards = self.extendPath(board, self.opponent(self.side))

        if not nextBoards:
            if isMax:
                return -float("inf")
            else:
                return float("inf")

        values = []
        newAlpha = alpha
        newBeta = beta
        for nextBoard in nextBoards:
            if values:
                if isMax:
                    if max(values) >= beta:
                        break
                    if max(values) > alpha:
                        newAlpha = max(values)
                else:
                    if min(values) <= alpha:
                        break
                    if min(values) < beta:
                        newBeta = min(values)

            values.append(self.minimax(nextBoard, depth + 1, newAlpha, newBeta))

        if isMax:
            return max(values)
        else:
            return min(values)



game = Konane(8)
#game.playOneGame(RandomPlayer(8),RandomPlayer(8),1)
#game.playOneGame(HumanPlayer(),RandomPlayer(8),1)
game.playOneGame(MinimaxPlayer(8,3),MinimaxPlayer(8,3),1)
