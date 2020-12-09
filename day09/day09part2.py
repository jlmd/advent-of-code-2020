def find_incorrect_number(numbers, preamble):
    for i in range(preamble, len(numbers)):
        if not find_two_numbers_sum(numbers[i - preamble:i], numbers[i]):
            return numbers[i]
    return -1


def find_two_numbers_sum(numbers, sum):
    rem_dict = {}
    for i in numbers:
        if i in rem_dict:
            return True
        rem_dict[sum - i] = i

    return False


if __name__ == '__main__':
    numbers = []
    with open('input.txt', 'r') as f:
        line = f.readline()
        while line:
            numbers.append(int(line))
            line = f.readline()

    preamble = 25
    incorrect_number = find_incorrect_number(numbers, preamble)
    sum = numbers[0]
    left = 0
    for right in range(1, len(numbers)):
        while sum > incorrect_number and right > left + 1:
            sum -= numbers[left]
            left += 1
        if sum == incorrect_number:
            range = numbers[left:right]
            print(min(range) + max(range))
            break
        sum += numbers[right]
