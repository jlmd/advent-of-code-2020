if __name__ == '__main__':
    joltage_ratings = []
    with open('input.txt', 'r') as f:
        line = f.readline()
        while line:
            joltage_ratings.append(int(line))
            line = f.readline()

    joltage_ratings.append(0)
    joltage_ratings.append(max(joltage_ratings) + 3)
    joltage_ratings.sort()
    dp = [0] * len(joltage_ratings)
    dp[0] = 1
    for i in range(1, len(joltage_ratings)):
        for j in range(1, 4):
            if i - j >= 0 and (joltage_ratings[i] - joltage_ratings[i - j]) in range(1, 4):
                dp[i] += dp[i - j]

    print(dp[len(dp) - 1])
