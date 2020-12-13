import math

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        estimate_timestamp = int(f.readline())
        buses = list(map(int, f.readline().replace(",x", "").split(",")))

    earliest_bus = 0
    earliest_bus_time_diff = estimate_timestamp
    for bus in buses:
        div = math.ceil(estimate_timestamp / bus)
        bus_diff = (bus * div) - estimate_timestamp
        if bus_diff < earliest_bus_time_diff:
            earliest_bus_time_diff = bus_diff
            earliest_bus = bus

    print(earliest_bus * earliest_bus_time_diff)
