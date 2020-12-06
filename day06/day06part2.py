def count_common_chars_in_all_groups(chars):
    chars_occ = {}
    for line in chars:
        for char in line:
            chars_occ[char] = chars_occ.get(char, 0) + 1
    return len({key: value for (key, value) in chars_occ.items() if value == len(chars)})


if __name__ == '__main__':
    chars_count = 0
    with open('input.txt', 'r') as f:
        line = f.readline()
        chars = []
        while line:
            if line != "\n":
                chars.append(line.replace("\n", ''))
            else:
                chars_count += count_common_chars_in_all_groups(chars)
                chars = []
            line = f.readline()
    chars_count += count_common_chars_in_all_groups(chars)
    print chars_count
