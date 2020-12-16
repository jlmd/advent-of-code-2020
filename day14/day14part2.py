import re


def dec_to_bin(dec):
    return '{:036b}'.format(dec)


def bin_to_dec(bin):
    return int(bin, 2)


def apply_mask(mask, mem):
    binary = dec_to_bin(mem)
    mem_value = list(36 * [0])
    x_positions = []
    for i in range(len(binary)):
        mask_value = mask[i]
        if mask_value == "X":
            x_positions.append(i)
        elif mask_value == "1":
            mem_value[i] = "1"
        elif mask_value == "0":
            mem_value[i] = binary[i]
    mem_values = []
    if len(x_positions) == 0:
        mem_values.append(bin_to_dec("".join(mem_value)))
    else:
        memory_addresses = []
        generate_combinations(mem_value, 0, x_positions, memory_addresses)
        for address in memory_addresses:
            mem_values.append(bin_to_dec("".join(address)))
    return mem_values


def generate_combinations(arr, i, x_positions, arr_generations):
    if i == len(x_positions):
        arr_generations.append(arr.copy())
        return
    arr[x_positions[i]] = "0"
    generate_combinations(arr, i + 1, x_positions, arr_generations)
    arr[x_positions[i]] = "1"
    generate_combinations(arr, i + 1, x_positions, arr_generations)


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
                decs_after_mask = apply_mask(mask, int(mem_dir))
                for dec in decs_after_mask:
                    mem_values[dec] = mem_value_dec

            line = f.readline()

    sum = 0
    for key in mem_values:
        sum += mem_values[key]
    print(sum)
