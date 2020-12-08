import copy


def switch_next_instruction(instructions, current_index):
    i = current_index
    while i < len(instructions):
        if instructions[i].operation == "nop":
            instructions[i].operation = "jmp"
            i += 1
            break
        elif instructions[i].operation == "jmp":
            instructions[i].operation = "nop"
            i += 1
            break
        i += 1

    return instructions, i


def execute_instructions(instructions):
    i = 0
    acc = 0
    while i < len(instructions):
        instruction = instructions[i]
        if instruction.executed:
            return False, 0
        if instruction.operation == "acc":
            acc += instruction.argument
            i += 1
        elif instruction.operation == "jmp":
            i += instruction.argument
        else:
            i += 1
        instruction.executed = True
    return True, acc


class Instruction:
    executed = False

    def __init__(self, operation, argument):
        self.operation = operation
        self.argument = argument

    def __str__(self):
        return self.operation + " " + str(self.argument)

    def __repr__(self):
        return str(self)


if __name__ == '__main__':
    instructions = []
    with open('input.txt', 'r') as f:
        line = f.readline()
        while line:
            instruction = line.split()
            operation = instruction[0]
            argument = int(instruction[1])
            instructions.append(Instruction(operation, argument))
            line = f.readline()

    change_index = 0
    instructions_original = copy.deepcopy(instructions)
    result, acc = execute_instructions(instructions)
    while result is False and change_index < len(instructions):
        instructions, change_index = switch_next_instruction(copy.deepcopy(instructions_original), change_index)
        result, acc = execute_instructions(instructions)

    print(acc)
