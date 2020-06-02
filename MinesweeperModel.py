from Tile import Tile


class MinesweeperModel:

    def __init__(self, difficulty='easy'):
        self.board = []
        self.board_size
        # Example of how to modify the fields of an object
        tile = Tile()
        tile.bomb = True
        tile.number_of_neighbour_bombs += 1

        # Function1 Get_board_size: input one of (easy, medium, hard)
        # returns x and y dimensions (width and height of the board)

        # Function2 Get_number_of_bombs: input one of (easy, medium, hard)
        # returns number of bombs

        # Function3 Build_board: input x and y
        # returns list of lists(a two-dimensional list) of default tile objects

        # Function4 Get_position_of_bombs: input number of bombs N and number of tile objects X * Y
        # returns N random distinct numbers between 0 and X * Y exclusive(meaning -1) [0, X*Y)

        # Function5 Assign_bombs_to_tiles: input board and bomb indexes from Function4
        # returns board with bomb tiles assigned.

        # Function6 Assign_numbers_to_tiles: input board from Function5
        # returns board with tile numbers assigned.


        # for i in range(0,x):
        #     for j in range(0,y):
        if difficulty not in ['easy','medium','hard']:
            raise ValueError("Reenter difficulty")
        if difficulty == 'easy':
            x == 8
            y == 10
        elif difficulty == 'medium':
            x ==
            y ==
        else:
            x ==
            y ==


        # list of lists of Tile

    # board (size(x,y choice by the user)) (3 choices : easy,medium,hard)

    # number of bombs,numbers,flags(graphic),question marks(graphic)
    #
    # _ _ _
    # _ _ _
    # _ _ _
    #

    # game over : 1)all revealed except for the bombs(win) 2)when user clicks a bomb tile(lose)
    # bombs placed randomly
    # the numbers are calculated AFTER bomb assignment
