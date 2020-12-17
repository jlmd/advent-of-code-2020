class Range:

    def __init__(self, range_from, range_to):
        self.range_from = range_from
        self.range_to = range_to

    def is_in_range(self, number):
        return self.range_from <= number <= self.range_to

    def __str__(self):
        return str(self.range_from) + "-" + str(self.range_to)


if __name__ == '__main__':
    ranges = []
    invalid_tickets = []
    with open('input.txt', 'r') as f:
        line = f.readline()
        # Ranges
        while line and line != "\n":
            line_split = line.replace("\n", "").split(":")[1].split()
            range1 = [int(n) for n in line_split[0].split("-")]
            range2 = [int(n) for n in line_split[2].split("-")]
            ranges.append(Range(range1[0], range1[1]))
            ranges.append(Range(range2[0], range2[1]))
            line = f.readline()
        # Ignore your ticket
        for i in range(4):
            f.readline()
        # Nearby tickets
        line = f.readline()
        while line:
            for ticket in line.replace("\n", "").split(","):
                in_range = False
                for curr_range in ranges:
                    if curr_range.is_in_range(int(ticket)):
                        in_range = True
                        break
                if not in_range:
                    invalid_tickets.append(int(ticket))
            line = f.readline()
    print(sum(invalid_tickets))