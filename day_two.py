PUZZLE_INPUT = (
    1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,6,19,1,19,5,23,2,13,23,27,1,10,27,31,2,6,31,35,1,9,35,39,2,10,39,43,1,43,9,47,1,
    47,9,51,2,10,51,55,1,55,9,59,1,59,5,63,1,63,6,67,2,6,67,71,2,10,71,75,1,75,5,79,1,9,79,83,2,83,10,87,1,87,6,91,1,13,
    91,95,2,10,95,99,1,99,6,103,2,13,103,107,1,107,2,111,1,111,9,0,99,2,14,0,0
)
LEGAL_OPCODES = (1, 2, 99)


def _init_memory(opcode=PUZZLE_INPUT[0], first=PUZZLE_INPUT[1], second=PUZZLE_INPUT[2], third=PUZZLE_INPUT[3]):
    intcode = list(PUZZLE_INPUT)
    intcode[0] = opcode
    intcode[1] = first
    intcode[2] = second
    intcode[3] = third
    return intcode


def process_intcode(**kwargs):
    intcode = _init_memory(**kwargs)
    try:
        i = 0
        while intcode[i] != 99:
            if intcode[i] == 1:
                intcode[intcode[i + 3]] = intcode[intcode[i + 1]] + intcode[intcode[i + 2]]
                i += 4
            elif intcode[i] == 2:
                intcode[intcode[i + 3]] = intcode[intcode[i + 1]] * intcode[intcode[i + 2]]
                i += 4
            elif intcode[i] not in LEGAL_OPCODES:
                raise RuntimeError('Encountered illegal opcode (legal opcodes: {0}, got: {1})! Aborting.'.format(
                    LEGAL_OPCODES, intcode[i]
                ))
        else:
            return intcode[0]
    except IndexError:
        print('Attempted to assign to index outside of intcode range!')
        raise


def find_params(desired_output):
    for noun in range(100):
        for verb in range(100):
            if process_intcode(first=noun, second=verb) == desired_output:
                return noun, verb


if __name__ == '__main__':
    result = process_intcode(first=12, second=2)
    print(result)  # 2692315

    first_param, second_param = find_params(19690720)
    print(100 * first_param + second_param)  # 9507
