class Interpreter:
    def __init__(self):
        self.registers = {}
        self.instructions = {
            'mov': self.mov,
            'inc': self.inc,
            'dec': self.dec,
            'jnz': self.jnz
        }
        self.pc = 0

    def mov(self, x, y):
        self.registers[x] = self.registers[y] if y in self.registers else int(y)
        self.pc += 1

    def inc(self, x):
        self.registers[x] += 1
        self.pc += 1

    def dec(self, x):
        self.registers[x] -= 1
        self.pc += 1

    def jnz(self, x, y):
        if x in self.registers:
            if self.registers[x] != 0:
                self.pc += self.registers[y] if y in self.registers else int(y)
            else:
                self.pc += 1
        else:
            if x != 0:
                self.pc += self.registers[y] if y in self.registers else int(y)
            else:
                self.pc += 1

    def run(self, program):
        while self.pc < len(program):
            args = program[self.pc].split()
            instruction = args[0]
            args.remove(instruction)
            self.instructions[instruction](*args)
        return self.registers


if __name__ == '__main__':
    interpreter = Interpreter()
    print(interpreter.run(['mov a 5', 'inc a', 'dec a', 'dec a', 'jnz a -1', 'inc a']))
