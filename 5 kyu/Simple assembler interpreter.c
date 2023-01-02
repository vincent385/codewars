#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include <string.h>
#include <ctype.h>

enum { MOV, INC, DEC, JNZ };

int getOpCodeFromInstruction(const char *instruction);
int extractInt32(const char *string);

void simple_assembler (size_t n, const char *const program[n], int registers[]) {
    size_t offset = 0;
    while (offset < n) {
        char instruction[4] = {};
        memcpy(instruction, program[offset], 3);
        int opcode = getOpCodeFromInstruction(instruction);
        switch (opcode) {
            case -1:
                printf("fatal error: bad instruction '%s'\n", instruction);
                exit(-1);
            case 0:
                registers[(unsigned) program[offset][4]] = extractInt32(program[offset]);
                offset += 1;
                break;
            case 1:
                registers[(unsigned) program[offset][4]] += 1;
                offset += 1;
                break;
            case 2:
                registers[(unsigned) program[offset][4]] -= 1;
                offset += 1;
                break;
            case 3:
                if (registers[(unsigned) program[offset][4]] != 0) {
                    int a = extractInt32(program[offset]);
                    if (program[offset][6] == '-') {
                        offset -= a;
                        break;
                    } else {
                        offset += a;
                        break;
                    }
                } else {
                    offset += 1;
                    break;
                }
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

int extractInt32(const char *string) {
    int val = 0;
    for (size_t i = 0; i < strlen(string); i++) {
        if (isdigit(string[i]))
            val = val * 10 + string[i] - '0';
    }
    return val;
}

int main (void) {
    const char *const program[6] = { "mov a 5", "inc a", "dec a", "dec a", "jnz a -1", "inc a" };
    int registers[96+26] = {};
    simple_assembler(6, program, registers);
    printf("register a: %d, register b: %d\n", registers['a'], registers['b']);
    return 0;
}
