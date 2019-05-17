class Board:
    def __init__(self):
        self.board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.current_mark = 'x'

    def __str__(self):
        out = '_______\n'
        for row in self.board:
            out += '|{}|{}|{}|\n'.format(row[0], row[1], row[2])
        out += '▔▔▔▔'
        return out

    def player(self):
        return self.current_mark

    def mark(self, x, y):
        # top left cell of the board is (1,1), bottom right is (3,3)
        if x < 1 or x > 3 or y < 1 or y > 3:
            raise ValueError('Invalid coordinates ({}, {})'.format(x, y))
        if self.board[y-1][x-1] == ' ':
            self.board[y-1][x-1] = self.current_mark
            self.current_mark = 'o' if self.current_mark == 'x' else 'x'
        else:
            raise ValueError('Invalid move, cell ({}, {}) is occupied'.format(x, y))

    # returns winner 'x', 'o', 'running' or 'tie'
    def status(self):
        for row in self.board:
            if row.count('o') == 3:
                return 'o'
            elif row.count('x') == 3:
                return 'x'
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] and self.board[0][col] != ' ':
                return self.board[0][col]
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != ' ':
            return self.board[0][0]
        if self.board[2][0] == self.board[1][1] == self.board[0][2] and self.board[2][0] != ' ':
            return self.board[2][0]
        for row in self.board:
            if ' ' in row:
                return "running"
        return "tie"


class Game:
    def __init__(self):
        self.board = Board()

    def start(self):
        while self.board.status() == "running":
            step = input('Player {}: '.format(self.board.player()))
            coord = step.split(',')
            try:
                # if an error occurs, the same player comes again
                self.board.mark(int(coord[0]), int(coord[1]))
            except ValueError as err:
                # if error is coming from the mark method or from converting str to int
                print(err)
            except IndexError:
                # if coordinates could not be split by ','
                print('Invalid coordinates {}'.format(coord))
            print(self.board)
        if self.board.status() == "tie":
            print('Game draw')
        else:
            print('Player {} won'.format(self.board.status()))


game = Game()
game.start()
