if __name__ == '__main__':
    joltage_ratings = []
    with open('input.txt', 'r') as f:
        line = f.readline()
        while line:
            joltage_ratings.append(int(line))
            line = f.readline()
    joltage_ratings.append(0)
    joltage_ratings.append(max(joltage_ratings) + 3)

    diffs = {}
    joltage_ratings.sort()
    for i in range(1, len(joltage_ratings)):
        diff = joltage_ratings[i] - joltage_ratings[i - 1]
        diffs[diff] = diffs.get(diff, 0) + 1
    print(diffs[1] * diffs[3])
