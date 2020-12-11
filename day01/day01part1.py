"""
 Problem:
    Find two numbers which sum 2020, and return the product of those numbers.
    Example:
        1721 979 366 299 675 1456
        1721 + 299 = 2020, so the result is 1721 * 299 = 514579

 Solution:
    Create a dict that will store the missing number for the sum of 2020.
    Iterate each number of the input:
        1. Check if current number is a key of the dict. In case it's it means that the sum is found, so return
            current number * value found in dict.
        2. Store 2020 - current number as key in map with current number as value.

    Complexity:
        Time: O(n)
        Space: O(n)
"""


def count_sum_pairs(values, expected_value):
    rem_dict = {}
    for i in values:
        if i in rem_dict:
            return i * rem_dict[i]
        rem_dict[expected_value - i] = i


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = f.read()
    entries = [int(i) for i in data.split()]
    print(count_sum_pairs(entries, 2020))
