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
    
    Find the free seat id where:
        - It's not in the very first or very last row 
        - Seats with IDs +1 and -1 from the seat are taken

 Solution:
    Read the input line by line, and for each line iterate the elements calculating the row and column:
    Keep pointers to the min row, max row, min col and max col
    For each element except last one of each type:
        If we need to take the higher part, we update the max element setting (min + max) / 2
        Otherwise, if we need to take the lower part, we update the min element setting (min + max) / 2
    For last element of each type (index 7 and 9)
        If we need to take the higher part, we know that the position is the max one
        Otherwise, if we need to take the lower part, we know that the position is the min one
        
    Keep an array bidimensional array of seats, where 1 indicates that it's taken and 0 indicates that it's free
    Calculate seat ids except the ones from first and last row
    Find the only free seat where seat id +1 and -1 are taken     

    Complexity:
        Time: O(n*m)
        Space: O(1)
"""


def get_seat_row_col(chars):
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
    return row, col


if __name__ == '__main__':
    seats = [[0 for x in range(8)] for y in range(128)]

    with open('input.txt', 'r') as f:
        line = f.readline()
        while line:
            row, col = get_seat_row_col(line)
            seats[row][col] = 1
            line = f.readline()

    free_ids = []
    for row in range(1, len(seats) - 1):
        for col in range(0, len(seats[row])):
            if seats[row][col] == 0:
                free_ids.append(row * 8 + col)

    for i in range(0, len(free_ids)):
        if (i == 0 or free_ids[i - 1] != free_ids[i] - 1) and \
                (i == len(free_ids) - 1 or free_ids[i + 1] != free_ids[i] + 1):
            print(free_ids[i])
