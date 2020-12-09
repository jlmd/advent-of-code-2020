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
    for i in range(preamble, len(numbers)):
        if not find_two_numbers_sum(numbers[i - preamble:i], numbers[i]):
            print(numbers[i])
            break
