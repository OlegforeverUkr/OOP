class Chess:
    color = 'white'  # default color the chess piece
    position = (0, 0)  # default position the chess piece

    def change_color(self) -> None:  # change the color of the chess piece
        if self.color == "white":
            self.color = "black"
        else:
            self.color = "white"

    def change_position(self, new_position: tuple) -> None:  # change the position of the chess piece, if possible
        if 0 <= new_position[0] <= 7 and 0 <= new_position[1] <= 7:
            self.position = (new_position[0], new_position[1])
        else:
            print("Invalid position. Position coordinates should be between 0 and 7.")

    def check_move(self, new_position: tuple) -> bool:  # checking the ability to make a move
        if 0 <= new_position[0] <= 7 and 0 <= new_position[1] <= 7:
            return True
        else:
            return False


class Pawn(Chess):

    def move(self, new_position: tuple):  # move method for Pawn
        self.old_position = self.position
        x, y = self.position
        new_x, new_y = new_position

        if self.color == 'white' and self.check_move(new_position):  # possibility of a move for white
            if x == new_x and new_y - y == 1:
                self.position = (new_x, new_y)
                print('You make a move')
            else:
                print("Can't make this move")
                self.position = self.old_position

        elif self.color == 'black' and self.check_move(new_position):  # possibility of a move for black
            if x == new_x and new_y - y == -1:
                self.position = (new_x, new_y)
                print('You make a move')
            else:
                print("Can't make this move")
                self.position = self.old_position


class King(Chess):

    def move(self, new_position: tuple):  # move method for King
        self.old_position = self.position
        x, y = self.position
        new_x, new_y = new_position

        if self.check_move(new_position):
            if -1 >= new_x - x <= 1 and -1 >= new_y - y <= 1:
                self.position = (new_x, new_y)
                print('You make a move')
            else:
                print("Can't make this move")
                self.position = self.old_position


class Rook(Chess):

    def move(self, new_position: tuple):  # move method for Rook
        self.old_position = self.position
        x, y = self.position
        new_x, new_y = new_position

        if self.check_move(new_position):
            if (x == new_x and y != new_y) or (x != new_x and y == new_y):
                self.position = (new_x, new_y)
                print('You make a move')
            else:
                print("Can't make this move")
                self.position = self.old_position


class Bishop(Chess):

    def move(self, new_position: tuple):  # move method for Bishop
        self.old_position = self.position
        x, y = self.position
        new_x, new_y = new_position

        if self.check_move(new_position):
            if new_x - x == new_y - y:
                self.position = (new_x, new_y)
                print('You make a move')
            else:
                print("Can't make this move")
                self.position = self.old_position


class Queen(Chess):

    def move(self, new_position: tuple):  # move method for Queen
        self.old_position = self.position
        x, y = self.position
        new_x, new_y = new_position

        if self.check_move(new_position):
            if (x == new_x and y != new_y) or (x != new_x and y == new_y) or (new_x - x == new_y - y):
                self.position = (new_x, new_y)
                print('You make a move')
            else:
                print("Can't make this move")
                self.position = self.old_position
        else:
            print("Can't make this move")
            self.position = self.old_position


t1 = Bishop()
t1.position = (4, 0)
t1.move((5, 1))
print(t1.position)
