import math

"""
 Problem:
    A seat might be specified like FBFBBFFRLR, where F means "front", B means "back", L means "left", and R means
    "right".

    The first 7 characters will either be F or B; these specify exactly one of the 128 rows on the plane (numbered 0
    through 127). Each letter tells you which half of a region the given seat is in. Start with the whole list of rows;
    the first letter indicates whether the seat is in the front (0 through 63) or the back (64 through 127). The next
    letter indicates which half of that region the seat is in, and so on until you're left with exactly one row.

    The last three characters will be either L or R; these specify exactly one of the 8 columns of seats on the plane
    (numbered 0 through 7). The same process as above proceeds again, this time with only three steps. L means to keep
    the lower half, while R means to keep the upper half.

    Example:
    For example, consider just the first seven characters of FBFBBFFRLR:
    
    Start by considering the whole range, rows 0 through 127.
       - F means to take the lower half, keeping rows 0 through 63.
       - B means to take the upper half, keeping rows 32 through 63.
       - F means to take the lower half, keeping rows 32 through 47.
       - B means to take the upper half, keeping rows 40 through 47.
       - B keeps rows 44 through 47.
       - F keeps rows 44 through 45.
       - R means to take the upper half, keeping columns 4 through 7.
       - L means to take the lower half, keeping columns 4 through 5.
       - The final R keeps the upper of the two, column 5.

    So, decoding FBFBBFFRLR reveals that it is the seat at row 44, column 5.

    In this example, the seat has ID 44 * 8 + 5 = 357

 Solution:
    Read the input line by line, and for each line iterate the elements calculating the row and column:
    Keep pointers to the min row, max row, min col and max col
    For each element except last one of each type:
        If we need to take the higher part, we update the max element setting (min + max) / 2
        Otherwise, if we need to take the lower part, we update the min element setting (min + max) / 2
    For last element of each type (index 7 and 9)
        If we need to take the higher part, we know that the position is the max one
        Otherwise, if we need to take the lower part, we know that the position is the min one

    Complexity:
        Time: O(n*m)
        Space: O(1)
"""


def day05part1(chars):
    min_row = 0
    max_row = 127
    min_col = 0
    max_col = 7
    for index in range(0, 7):
        char = chars[index]
        if char == 'F':
            max_row = int(math.floor((min_row + max_row) / 2.0))
        elif char == 'B':
            min_row = int(math.ceil((min_row + max_row) / 2.0))
    for index in range(7, 9):
        char = chars[index]
        if char == 'L':
            max_col = int(math.floor((min_col + max_col) / 2.0))
        elif char == 'R':
            min_col = int(math.ceil((min_col + max_col) / 2.0))
    if chars[7] == 'F':
        row = min_row
    else:
        row = max_row
    if chars[9] == 'L':
        col = min_col
    else:
        col = max_col
    return row * 8 + col


if __name__ == '__main__':
    highest_seat_id = 0
    with open('input.txt', 'r') as f:
        line = f.readline()
        while line:
            seat_id = day05part1(line)
            highest_seat_id = max(seat_id, highest_seat_id)
            line = f.readline()
    print highest_seat_id
