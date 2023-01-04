#include <stdlib.h>
#include <string.h>
#include <ctype.h>

// op codes
enum ops { MOV, INC, DEC, JNZ };

// prototypes
int getOpCodeFromInstruction(const char *instruction);
int getValue(char *str, int registers[]);
void mov(unsigned x, int y, int registers[]);
void inc(unsigned x, int registers[]);
void dec(unsigned x, int registers[]);
int jnz(int x, int y);

void simple_assembler (size_t n, const char *const program[n], int registers[]) {
    char *delim = " ";
    size_t pc = 0;
    while (pc < n) {
        char *str = malloc(strlen(program[pc]) * sizeof(char) + 1);
        strcpy(str, program[pc]);
        char *arg = strtok(str, delim);
        int opcode = getOpCodeFromInstruction(arg);
        switch (opcode) {
            case 0:
                arg = strtok(NULL, delim);
                mov(arg[0], getValue(strtok(NULL, delim), registers), registers);
                pc++;
                break;
            case 1:
                arg = strtok(NULL, delim);
                inc(arg[0], registers);
                pc++;
                break;
            case 2:
                arg = strtok(NULL, delim);
                dec(arg[0], registers);
                pc++;
                break;
            case 3:
                arg = strtok(NULL, delim);
                pc += jnz(getValue(arg, registers), getValue(strtok(NULL, delim), registers));
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

int getValue(char *str, int registers[]) {
    unsigned c = str[0];
    if (isalpha(c)) 
        return registers[c];
    else
        return atoi(str);
}

void mov(unsigned x, int y, int registers[]) { registers[x] = y; }

void inc(unsigned x, int registers[]) { registers[x]++; }

void dec(unsigned x, int registers[]) { registers[x]--; }

int jnz(int x, int y) {
    if (x != 0)
        return y;
    else
        return 1;
}
