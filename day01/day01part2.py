"""
 Problem:
    Find three numbers which sum 2020, and return the product of those numbers.
    Example:
        1721 979 366 299 675 1456
        979 + 366 + 675 = 2020, so the result is 979 * 366 * 675 = 2020 = 241861950

 Solution:
    Create a dict that will store the missing number for the sum of 2020 as key and the list of two numbers as value
    1. Iterate each number of the input:
        For each number, iterate all the other numbers:
            Add 2020 - the sum of each pair of number as key and both numbers as value

    2. Iterate each number of the input:
        1. Check if current number is a key of the dict. In case it's it means that the sum is found, so return
            current number * the two numbers found in dict

    Complexity:
        Time: O(n^2)
        Space: O(n^2)
"""


def day01part2(values):
    rem_dict = {}
    for i in values:
        for j in values:
            rem_dict[2020 - i - j] = [i, j]

    for i in values:
        if i in rem_dict:
            print(i * rem_dict[i][0] * rem_dict[i][1])
            return


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = f.read()
    entries = [int(i) for i in data.split()]
    day01part2(entries)
