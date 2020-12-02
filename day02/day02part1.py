"""
 Problem:
    Check how many passwords are valid. A valid password is a password that contains the indicated letter inside a
    range of occurrences.
    Example:
        1-3 a: abcde
        1-3 b: cdefg
        2-9 c: ccccccccc

        In the example there are 2 valid passwords. The middle password, cdefg, is not; it contains no instances of b,
        but needs at least 1. The first and third passwords are valid: they contain one a or nine c, both within the
        limits of their respective policies.

 Solution:
    Read the input line by line, gathering the necessary data: lowest, highest, letter, password
    For each line, check if the occurrences of the letter in the password is inside the provided range.

    Complexity:
        Time: O(n)
        Space: O(1)
"""


def day02part1(lowest, highest, letter, password):
    letter_occurrences = 0
    for ch in password:
        if ch == letter:
            letter_occurrences += 1
    return letter_occurrences in range(lowest, highest + 1)


if __name__ == '__main__':
    valid_passwords = 0
    with open('input.txt', 'r') as f:
        line = f.readline()
        while line:
            data = line.split()
            lowest_range = int(data[0].split("-")[0])
            highest_range = int(data[0].split("-")[1])
            letter = data[1][:-1]
            password = data[2]
            if day02part1(lowest_range, highest_range, letter, password):
                valid_passwords += 1
            line = f.readline()
    print(valid_passwords)
