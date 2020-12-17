import collections

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        numbers = [int(n) for n in f.readline().split(",")]

    spoken_numbers = {}
    for i in range(len(numbers)):
        pos = numbers[i]
        spoken_numbers[pos] = collections.deque(maxlen=2)
        spoken_numbers[pos].append(i)
    prev_number = numbers[-1]
    turn_to_find = 30000000
    for i in range(len(numbers), turn_to_find):
        if prev_number in spoken_numbers and len(spoken_numbers[prev_number]) == 2:
            prev_number = spoken_numbers[prev_number][1] - spoken_numbers[prev_number][0]
        else:
            prev_number = 0
        if prev_number not in spoken_numbers:
            spoken_numbers[prev_number] = collections.deque(maxlen=2)
        spoken_numbers[prev_number].append(i)
        if i == turn_to_find - 1:
            print(prev_number)
