#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

enum { MOV, INC, DEC, JNZ };

int getOpCodeFromInstruction(const char *instruction);
int extractInt32(const char *string, size_t sidx);
unsigned fastLog10(unsigned x);

void simple_assembler (size_t n, const char *const program[n], int registers[]) {
    size_t offset = 0;
    while (offset < n) {
        char instruction[4] = {};
        memcpy(instruction, program[offset], 3);
        int opcode = getOpCodeFromInstruction(instruction);
        unsigned reg = program[offset][4];
        unsigned treg = program[offset][6];
        int a, b;
        switch (opcode) {
            case -1:
                printf("fatal error: bad instruction '%s'\n", instruction);
                exit(-1);
            case 0:
                if (isdigit(treg) || treg == '-') {
                    if (treg == '-')
                        registers[reg] = -extractInt32(program[offset], 5);
                    else
                        registers[reg] = extractInt32(program[offset], 5);
                } else {
                    unsigned treg = program[offset][6];
                    registers[reg] = registers[treg];
                }
                offset += 1;
                break;
            case 1:
                registers[reg] += 1;
                offset += 1;
                break;
            case 2:
                registers[reg] -= 1;
                offset += 1;
                break;
            case 3:
                if (isdigit(reg) || reg == '-') {
                    if (reg == '-')
                        a = -extractInt32(program[offset], 3);
                    else
                        a = extractInt32(program[offset], 3);
                } else
                    a = registers[reg];

                if (isdigit(treg) || treg == '-') {
                    if (treg == '-')
                        b = -extractInt32(program[offset], 5 + fastLog10(a));
                    else
                        b = extractInt32(program[offset], 5 + fastLog10(a));
                } else
                    b = registers[reg];

                if (a != 0)
                    offset += b;
                else
                    offset += 1;

                break;
        }
    }
}

int getOpCodeFromInstruction(const char *instruction) {
    if (strcmp(instruction, "mov") == 0)
        return MOV;
    else if (strcmp(instruction, "inc") == 0)
        return INC;
    else if (strcmp(instruction, "dec") == 0)
        return DEC;
    else if (strcmp(instruction, "jnz") == 0)
        return JNZ;
    return -1;
}

int extractInt32(const char *string, size_t sidx) {
    int val = 0;
    for (size_t i = sidx; i < strlen(string); i++) {
        if (isdigit(string[i]))
            val = val * 10 + string[i] - '0';
    }
    return val;
}

unsigned fastLog10(unsigned x) {
    return (x >= 1000000000) ? 9 : (x >= 100000000) ? 8 : (x >= 10000000) ? 7 : 
    (x >= 1000000) ? 6 : (x >= 100000) ? 5 : (x >= 10000) ? 4 : (x >= 1000) ? 3 :
    (x >= 100) ? 2 : (x >= 10) ? 1 : 0;
}

int main (void) {
    const char *const program[6] = { "mov a 25", "inc a", "dec a", "dec a", "jnz a -1", "inc a" };
    int registers[26];
    simple_assembler(6, program, registers);
    printf("register a: %d, register b: %d\n", registers['a'], registers['b']);
    return 0;
}
