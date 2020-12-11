from copy import copy, deepcopy


def get_adjacent_occupied_seats(x, y, seats):
    adjacent_count = 0
    x_dirs = [-1, 0, 1]
    y_dirs = [-1, 0, 1]
    for i in range(0, len(x_dirs)):
        for j in range(0, len(y_dirs)):
            new_x = x + x_dirs[i]
            new_y = y + y_dirs[j]
            if (new_x == x and new_y == y) or new_x < 0 or new_x >= len(seats) or new_y < 0 or new_y >= len(seats[0]):
                continue
            if seats[new_x][new_y] == "#":
                adjacent_count += 1
    return adjacent_count


def seat_round(seats):
    updated_seats = deepcopy(seats)
    seats_changed = False
    occupied_seats = 0
    for i in range(0, len(seats)):
        for j in range(0, len(seats[i])):
            adjacent_occupied_seats = get_adjacent_occupied_seats(i, j, seats)
            if seats[i][j] == "L" and adjacent_occupied_seats == 0:
                updated_seats[i][j] = "#"
                seats_changed = True
            elif seats[i][j] == "#" and adjacent_occupied_seats >= 4:
                updated_seats[i][j] = "L"
                seats_changed = True
            if seats[i][j] == "#":
                occupied_seats += 1
    return seats_changed, occupied_seats, updated_seats


if __name__ == '__main__':
    seats = []
    with open('input.txt', 'r') as f:
        line = f.readline()
        while line:
            seats.append(list(line.replace("\n", '')))
            line = f.readline()

    seats_changed, occupied_seats, seats = seat_round(seats)
    while seats_changed:
        seats_changed, occupied_seats, seats = seat_round(seats)

    print(occupied_seats)
