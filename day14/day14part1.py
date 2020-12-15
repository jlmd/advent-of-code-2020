import re


def dec_to_bin(dec):
    return bin(dec)[2:]


def bin_to_dec(bin):
    return int(bin, 2)


def apply_mask(mask, mem):
    binary = dec_to_bin(mem)
    mem_value = list(mask.replace("X", "0"))
    for i in range(0, len(binary)):
        if mask[len(mask) - 1 - i] == "X":
            mem_value[len(mem_value) - 1 - i] = binary[len(binary) - 1 - i]
    return "".join(mem_value)


if __name__ == '__main__':
    mem_values = {}
    with open('input.txt', 'r') as f:
        line = f.readline()
        while line:
            if line.__contains__("mask"):
                mask = line[-37:].rstrip()
            else:
                mem_dir = re.search(r"\[([0-9]+)\]", line).group(1)
                mem_value_dec = int(line.rstrip().replace(" ", "").split("=")[1])
                mem_values[mem_dir] = apply_mask(mask, mem_value_dec)
            line = f.readline()

    sum = 0
    for key in mem_values:
        sum += bin_to_dec(str(mem_values[key]))
    print(sum)
