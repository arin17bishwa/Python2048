import random
import time


class Game:
    def __init__(self, side=4, target=2048):
        self.side_len = side
        self.board = [[0] * side for _ in range(side)]
        self.__score = 0
        self.target = 2048

        # initialise first 2 random blocks
        pos1, pos2 = random.sample(range(side * side), 2)
        self.board[pos1 // side][pos1 % side] = 2
        self.board[pos2 // side][pos2 % side] = 2

    def __blank_positions(self):
        """
        :returns list of tuples of blank positions in the board
        """
        mat = self.board
        positions = [(i, j) for i in range(self.side_len) for j in range(self.side_len) if mat[i][j] == 0]
        return positions

    def getScore(self):
        return self.__score

    def place_two(self):
        choice = random.choice(self.__blank_positions())
        self.board[choice[0]][choice[1]] = 2

    def shiftLeft(self):
        flag = 0
        for i in range(self.side_len):
            if 0 in self.board[i]:
                for j in range(self.side_len - 1):
                    if self.board[i][j] == 0:
                        k = j
                        while k < self.side_len - 1 and self.board[i][k] == 0:
                            k += 1
                            flag = 1
                        self.board[i][k], self.board[i][j] = self.board[i][j], self.board[i][k]
        return flag

    def addLeft(self):
        flag = 0
        for i in range(self.side_len):
            for j in range(self.side_len - 1):
                if self.board[i][j] == self.board[i][j + 1]:
                    flag = 1
                    self.board[i][j] += self.board[i][j + 1]
                    self.board[i][j + 1] = 0
                    self.__score += self.board[i][j]
        return flag

    def moveLeft(self):
        a = self.shiftLeft()
        b = self.addLeft()
        c = self.shiftLeft()
        return a + b + c != 0

    def shiftRight(self):
        flag = 0
        for i in range(self.side_len):
            for j in range(self.side_len - 1, 0, -1):
                if self.board[i][j] == 0:
                    k = j
                    while k > 0 and self.board[i][k] == 0:
                        k -= 1
                        flag = 1
                    self.board[i][k], self.board[i][j] = self.board[i][j], self.board[i][k]
        return flag

    def addRight(self):
        flag = 0
        for i in range(self.side_len):
            for j in range(self.side_len - 1, 0, -1):
                if self.board[i][j] == self.board[i][j - 1]:
                    flag = 1
                    self.board[i][j] += self.board[i][j - 1]
                    self.board[i][j - 1] = 0
                    self.__score += self.board[i][j]
        return flag

    def moveRight(self):
        a = self.shiftRight()
        b = self.addRight()
        c = self.shiftRight()
        return a + b + c != 0

    def shiftUp(self):
        flag = 0
        for j in range(self.side_len):
            for i in range(self.side_len - 1):
                if self.board[i][j] == 0:
                    k = i
                    while k < self.side_len - 1 and self.board[k][j] == 0:
                        k += 1
                        flag = 1
                    self.board[k][j], self.board[i][j] = self.board[i][j], self.board[k][j]
        return flag

    def addUp(self):
        flag = 0
        for j in range(self.side_len):
            for i in range(self.side_len - 1):
                if self.board[i][j] == self.board[i + 1][j]:
                    flag = 1
                    self.board[i][j] += self.board[i + 1][j]
                    self.board[i + 1][j] = 0
                    self.__score += self.board[i][j]
        return flag

    def moveUp(self):
        a = self.shiftUp()
        b = self.addUp()
        c = self.shiftUp()
        return a + b + c != 0

    def shiftDown(self):
        flag = 0
        for j in range(self.side_len):
            for i in range(self.side_len - 1, 0, -1):
                if self.board[i][j] == 0:
                    k = i
                    while k > 0 and self.board[k][j] == 0:
                        k -= 1
                        flag = 1
                    self.board[k][j], self.board[i][j] = self.board[i][j], self.board[k][j]
        return flag

    def addDown(self):
        flag = 0
        for j in range(self.side_len):
            for i in range(self.side_len - 1, 0, -1):
                if self.board[i][j] == self.board[i - 1][j]:
                    self.board[i][j] += self.board[i - 1][j]
                    self.board[i - 1][j] = 0
                    self.__score += self.board[i][j]
                    flag = 1
        return flag

    def moveDown(self):
        a = self.shiftDown()
        b = self.addDown()
        c = self.shiftDown()
        return a + b + c != 0

    def verdict(self):
        """
        :returns 0 if blank spaces are/will be available; 2 if game won; 1 if game lost
        """
        for i in range(self.side_len):
            if self.board[i][0] == 0:
                return 0
            elif self.board[i][0] == self.target:
                return 2
            for j in range(1, self.side_len):
                if self.board[i][j] == 0 or self.board[i][j] == self.board[i][j - 1]:
                    return 0
                elif self.board[i][j] == self.target:
                    return 2
        self.__score = 0
        return 1

    def __str__(self):
        arr = [[" ", "-" * (8 * self.side_len + 1)]]
        for row in range(self.side_len):
            arr.append([' | '])
            for col in range(self.side_len):
                if self.board[row][col] == 0:
                    arr[2 * row + 1].append(str((4 - len(str(self.board[row][col]))) * " " + str(" ")) + "  | ")
                else:
                    arr[2 * row + 1].append(
                        (4 - len(str(self.board[row][col]))) * " " + str(self.board[row][col]) + "  | ")
            arr.append((' ', "-" * (8 * self.side_len + 1)))

        return '\n'.join([''.join(i) for i in arr])


if __name__ == '__main__':
    games = []
    play = True
    while play:
        name = input('Enter your name: ')
        try:
            side_len = int(input('Enter length of side(min 4): '))
        except ValueError:
            print('Invalid input. It must be an integer. Using default value 4 instead.')
            side_len = 4
        target_score=pow(2,3*side_len-1)
        game = Game(side=max(4,side_len))
        playable = 0
        while playable == 0:
            print(game)
            mv = input('Enter your move: ').strip().lower()
            # print('Enter your move: {}'.format(mv))
            if mv == 'w':
                response = game.moveUp()
            elif mv == 's':
                response = game.moveDown()
            elif mv == 'a':
                response = game.moveLeft()
            elif mv == 'd':
                response = game.moveRight()
            else:
                print("Invalid input. Please enter 'w'/'a'/'s'/'d' to move.")
                continue

            playable = game.verdict()
            if playable:
                break

            if not response:
                print('Move not possible. Please choose another move.\n')
                continue
            game.place_two()
        print(game)
        if playable == 1:
            print('You lost.')
        else:
            print('You won.', playable)
        print('Score:', game.getScore())
        play = input('Wanna play again? Type "yes" if you want to: ').strip().lower() == 'yes'
