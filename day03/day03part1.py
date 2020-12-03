"""
 Problem:
    Given a grid of squares (.) and trees (#), count the trees starting from top left until reaching the bottom.
    Each move jumps 3 cells to right and 1 to down.
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
        In this example, traversing the map using this slope (right 3, down 1) would cause you to encounter 7 trees.

 Solution:
    Read the input line by line:
        Starting from second line, keep a pointer to maintain right index, which will be incremented by 3 for each line
        and will apply module the number of elements in first line.

    Complexity:
        Time: O(n)
        Space: O(1)
"""


def day03part1(line, position):
    return line[position] == '#'


if __name__ == '__main__':
    trees = 0
    with open('input.txt', 'r') as f:
        line = f.readline()
        width = len(line)
        right_index = 0
        while line:
            if day03part1(line, right_index):
                trees += 1
            right_index = (right_index + 3) % (width - 1)
            line = f.readline()
    print(trees)
