#
# board.py (Final project)
#

class Board:
    """ A class for objects that represent an Eight Puzzle board.
    """
    def __init__(self, digitstr):
        """ a constructor for a Board object whose configuration
            is specified by the input digitstr
            input: digitstr is a permutation of the digits 0-9
        """
        # check that digitstr is 9-character string
        # containing all digits from 0-9
        assert(len(digitstr) == 9)
        for x in range(9):
            assert(str(x) in digitstr)

        self.tiles = [[0] * 3 for x in range(3)]
        self.blank_r = -1
        self.blank_c = -1

        # Put your code for the rest of __init__ below.
        # Do *NOT* remove our code above.


    ### Add your other method definitions below. ###
# question 1
        for i in range(9):
            r = i // 3
            c = i % 3
            digit = int(digitstr[i])
            self.tiles[r][c] = digit
            if digit == 0:
                self.blank_r = r
                self.blank_c = c
                
                
# question 2
    def __repr__(self):
        representation = ""
        for row in self.tiles:
            for val in row:
                representation += '_' + ' ' if val == 0 else str(val) + ' '
            representation += '\n'
        return representation

# question 3
    def move_blank(self, direction):

        directions = {
            'up': (-1, 0),
            'down': (1, 0),
            'left': (0, -1),
            'right': (0, 1)
        }

        if direction not in directions:
            print(f"unknown direction: {direction}")
            return False

        dr, dc = directions[direction]
        new_r, new_c = self.blank_r + dr, self.blank_c + dc

        if new_r < 0 or new_r > 2 or new_c < 0 or new_c > 2:
            return False

        self.tiles[self.blank_r][self.blank_c], self.tiles[new_r][new_c] = self.tiles[new_r][new_c], self.tiles[self.blank_r][self.blank_c]
        
        self.blank_r, self.blank_c = new_r, new_c

        return True

# question 4
    def digit_string(self):
        return ''.join(str(self.tiles[r][c]) for r in range(3) for c in range(3))
    
# question 5
    def copy(self):
        return Board(self.digit_string())
    
# question 6
    def num_misplaced(self):
        count = 0

        goal = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

        for i in range(3):
            for j in range(3):
                if self.tiles[i][j] != 0 and self.tiles[i][j] != goal[i][j]:
                    count += 1

        return count
    
# question 7

    def __eq__(self, other):
        # Compare the 'tiles' attribute of self and other
        return self.tiles == other.tiles
    
    
#test function
if __name__ == '__main__':

    ## put test cases here:
    b = Board('142358607')
    print(b.tiles)
    print(b.blank_r)
    b2 = Board('631074852')
    print(b2.tiles)
    b = Board('142358607')
    print(b.tiles)
    print(b)
    b = Board('142358607')
    print(b)
    print(b.move_blank('up'))
    print(b)
    b = Board('142358607')
    print(b.digit_string())
    print(b.move_blank('right'))
    print(b.move_blank('up'))
    print(b.digit_string())
    b = Board('142358607')
    print(b)
    b2 = b.copy()
    print(b2)
    print(b2.move_blank('up'))
    print(b2)
    b = Board('142358607')
    print(b)
    print(b.num_misplaced())
    print(b.move_blank('right'))
    print(b)
    b1 = Board('012345678')
    b2 = Board('012345678')
    print(b1 == b2)
    b2.move_blank('right')
    print(b1 == b2)
    
    
    
    
    