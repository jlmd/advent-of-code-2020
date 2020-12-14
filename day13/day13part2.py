if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        f.readline()
        buses = list(map(int, f.readline().replace("x", "-1").split(",")))

    timestamps_diff = [0]
    for i in range(1, len(buses)):
        if buses[i] != -1:
            timestamps_diff.append(buses[i] - i)

    buses = list(filter(lambda bus: bus != -1, buses))

    print(list(map(lambda args: args[1] - timestamps_diff[args[0]], enumerate(buses))))
    i = 0
    # Brute force, takes too long
    while True:
        found = True
        i_increment = buses[0]
        for j in range(1, len(buses)):
            if i % buses[j] != timestamps_diff[j]:
                found = False
                continue
        if found:
            print(i)
            break
        i += buses[0]
