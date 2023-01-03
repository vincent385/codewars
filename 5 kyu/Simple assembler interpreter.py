def simple_assembler(program):
    reg_dict = {}
    lcharacters = 'abcdefghijklmnopqrstuvwxyz'
    offset = 0
    while offset < len(program):
        instruction = program[offset].split()
        if instruction[0] == 'mov':
            if instruction[2] in lcharacters:
                reg_dict[instruction[1]] = reg_dict[instruction[2]]
            else:
                reg_dict[instruction[1]] = int(instruction[2])
            offset += 1
        elif instruction[0] == 'inc':
            reg_dict[instruction[1]] += 1
            offset += 1
        elif instruction[0] == 'dec':
            reg_dict[instruction[1]] -= 1
            offset += 1
        elif instruction[0] == 'jnz':
            if instruction[1] in lcharacters:
                if reg_dict[instruction[1]] == 0:
                    offset += 1
                else:
                    if instruction[2] in lcharacters:
                        offset += reg_dict[instruction[2]]
                    else:
                        offset += int(instruction[2])
            else:
                if int(instruction[1]) == 0:
                    offset += 1
                else:
                    if instruction[2] in lcharacters:
                        offset += reg_dict[instruction[2]]
                    else:
                        offset += int(instruction[2])
    return reg_dict


if __name__ == '__main__':
    print(simple_assembler(['mov a 5', 'inc a', 'dec a', 'dec a', 'jnz a -1', 'inc a']))
