"""
 Problem:
    Check whether if provided letter is at position one or position two, but not in both.
    Example:
        1-3 a: abcde is valid: position 1 contains a and position 3 does not.
        1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
        2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.

 Solution:
    Read the input line by line, gathering the necessary data: position_one, position_two, letter, password
    For each line, check in the password if one of the following statement is true:
        - Position one contains the provided letter, and position two doesn't
        - Position doesn't contains the provided letter, and position two does

    Complexity:
        Time: O(1)
        Space: O(1)
"""


def day02part1(position_one, position_two, letter, password):
    return (password[position_one - 1] == letter and password[position_two - 1] != letter) or \
           (password[position_one - 1] != letter and password[position_two - 1] == letter)


if __name__ == '__main__':
    valid_passwords = 0
    with open('input.txt', 'r') as f:
        line = f.readline()
        while line:
            data = line.split()
            position_one = int(data[0].split("-")[0])
            position_two = int(data[0].split("-")[1])
            letter = data[1][:-1]
            password = data[2]
            if day02part1(position_one, position_two, letter, password):
                valid_passwords += 1
            line = f.readline()
    print(valid_passwords)
