def count_unique_chars(chars):
    chars_occ = {}
    for char in chars:
        chars_occ[char] = True
    return len(chars_occ)


if __name__ == '__main__':
    unique_chars_count = 0
    with open('input.txt', 'r') as f:
        line = f.readline()
        chars = ""
        while line:
            chars += line.replace("\n", "")
            if line == "\n":
                unique_chars_count += count_unique_chars(chars)
                chars = ""
            line = f.readline()
    unique_chars_count += count_unique_chars(chars)
    print(unique_chars_count)
