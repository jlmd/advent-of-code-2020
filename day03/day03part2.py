"""
 Problem:
    Given a grid of squares (.) and trees (#), count the trees from each slope starting from top left until reaching
    he bottom, and multiply them. Slopes:
        Right 1, down 1
        Right 3, down 1
        Right 5, down 1
        Right 7, down 1
        Right 1, down 2
    The grid is circular horizontally (the same pattern repeats to the right many times).

    Example:
        ..##.......
        #...#...#..
        .#....#..#.
        ..#.#...#.#
        .#...##..#.
        ..#.##.....
        .#.#.#....#
        .#........#
        #.##...#...
        #...##....#
        .#..#...#.#

       These slopes would find 2, 7, 3, 4, and 2 tree(s) respectively; multiplied together, these
       produce the answer 336.

 Solution:
    Use a class to represent each slope, having a reference to the current right index and the number of trees
    Read the input line by line and recalculate right index as:
     right_index = (right_index + right_movement) % (width - 1)

    Complexity:
        Time: O(n)
        Space: O(1)
"""


class Slope:
    trees = 0
    right_index = 0

    def __init__(self, right, down):
        self.right = right
        self.down = down

    def is_position_valid(self, down_index):
        return down_index % self.down == 0

    def move(self, max_right_index):
        self.right_index = (self.right_index + self.right) % max_right_index


def day03part1(line, position):
    return line[position] == '#'


if __name__ == '__main__':
    slopes = [Slope(1, 1), Slope(3, 1), Slope(5, 1), Slope(7, 1), Slope(1, 2)]
    with open('input.txt', 'r') as f:
        line = f.readline()
        width = len(line)
        down_index = 0
        while line:
            for slope in slopes:
                if slope.is_position_valid(down_index):
                    if day03part1(line, slope.right_index):
                        slope.trees += 1
                    slope.move(width - 1)
            down_index += 1
            line = f.readline()
    trees = 1
    for slope in slopes:
        trees *= slope.trees
    print(trees)
