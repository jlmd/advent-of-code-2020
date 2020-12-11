"""
 Problem:
    Find three numbers which sum 2020, and return the product of those numbers.
    Example:
        1721 979 366 299 675 1456
        979 + 366 + 675 = 2020, so the result is 979 * 366 * 675 = 241861950

 Solution:
    1. Sort numbers
    2. Iterate numbers
        For each number:
            Use two pointers to iterate the numbers starting from current + 1
            pointerLeft = current + 1
            pointerRight = numbers.length - 1
            while (pointerLeft < pointerRight)
                sum = numbers[currentNumber] + numbers[pointerLeft] + numbers[pointerRight]
                if (sum == 2020) result found
                else if (sum < 2020) pointerLeft++
                else pointerRight--

    Complexity:
        Time: O(n^2)
        Space: O(n)
"""


def count_sum_triplets(values, expected_value):
    values.sort()
    for i in range(0, len(values)):
        left = i + 1
        right = len(values) - 1
        while left < right:
            current_sum = values[i] + values[left] + values[right]
            if current_sum == expected_value:
                return values[i] * values[left] * values[right]
            elif current_sum < expected_value:
                left += 1
            else:
                right -= 1


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = f.read()
    entries = [int(i) for i in data.split()]
    print(count_sum_triplets(entries, 2020))
