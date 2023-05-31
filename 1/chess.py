class Chess:
    color = 'white'
    position = (0, 0)

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

    def check_move(self, new_position: tuple) -> bool:  # checks the possibility of a move
        self.change_position(new_position)
        return True


class Pawn(Chess):

    def move(self, new_position: tuple):
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


t1 = Pawn()
t1.position = (3, 2)
t1.move((3, 9))
# t2 = Pawn()
# t2.color = 'black'
# t2.position = (3, 6)
# t2.move((3, 5))
print(t1.position)
