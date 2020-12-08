class Instruction:
    executed = False

    def __init__(self, operation, argument):
        self.operation = operation
        self.argument = argument


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

    acc = 0
    i = 0
    while i < len(instructions):
        instruction = instructions[i]
        if instruction.executed:
            print(acc)
            break
        if instruction.operation == "acc":
            acc += instruction.argument
            i += 1
        elif instruction.operation == "jmp":
            i += instruction.argument
        else:
            i += 1
        instruction.executed = True
