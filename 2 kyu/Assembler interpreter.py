class Interpreter:
    def __init__(self):
        self.regs = {
            'ip': 0,
            'lr': 0
        }
        self.flags = {
            'zf': False,
            'sf': False
        }
        self.labels = {}
        self.instructions = {
            'mov': self.mov,
            'inc': self.inc,
            'dec': self.dec,
            'add': self.add,
            'sub': self.sub,
            'mul': self.mul,
            'div': self.div,
            'jmp': self.jmp,
            'cmp': self.cmp,
            'jne': self.jne,
            'je': self.je,
            'jge': self.jge,
            'jg': self.jg,
            'jle': self.jle,
            'jl': self.jl,
            'call': self.call,
            'ret': self.ret,
            'msg': self.msg,
            'end': self.end
        }

    def __preprocess__(self, code: str):
        # split code into lines
        lines = code.split('\n')
        # remove empty strings
        lines = [x.split() for x in lines if x.split()]
        # ignore comments and preprocess labels
        idx = 0
        while idx < len(lines):
            if ';' in lines[idx]:
                comment_idx = lines[idx].index(';')
                lines[idx] = lines[idx][:comment_idx]
            if lines[idx]:
                if lines[idx][0] not in self.instructions:
                    self.labels[lines[idx][0].replace(':', '')] = idx + 1
            else:
                lines.pop(idx)
            idx += 1
        return lines

    def __increment_instruction_pointer__(self):
        self.regs['ip'] += 1

    def get_value(self, val):
        return self.regs[val] if val in self.regs else int(val)

    def mov(self, x, y):
        self.regs[x] = self.get_value(y)
        self.__increment_instruction_pointer__()

    def inc(self, x):
        self.regs[x] += 1
        self.__increment_instruction_pointer__()

    def dec(self, x):
        self.regs[x] -= 1
        self.__increment_instruction_pointer__()

    def add(self, x, y):
        self.regs[x] += self.get_value(y)
        self.__increment_instruction_pointer__()

    def sub(self, x, y):
        self.regs[x] -= self.get_value(y)
        self.__increment_instruction_pointer__()

    def mul(self, x, y):
        self.regs[x] *= self.get_value(y)
        self.__increment_instruction_pointer__()

    def div(self, x, y):
        self.regs[x] /= self.get_value(y)
        self.__increment_instruction_pointer__()

    def jmp(self, lbl):
        self.regs['ip'] = self.labels[lbl]

    def cmp(self, x, y):
        result = self.get_value(x) - self.get_value(y)
        if result == 0:
            self.flags['zf'] = True
            self.flags['sf'] = False
        elif result < 0:
            self.flags['zf'] = False
            self.flags['sf'] = True
        else:
            self.flags['zf'] = False
            self.flags['sf'] = False
        self.__increment_instruction_pointer__()

    def jne(self, lbl):
        self.jmp(lbl) if not self.flags['zf'] else self.__increment_instruction_pointer__()

    def je(self, lbl):
        self.jmp(lbl) if self.flags['zf'] else self.__increment_instruction_pointer__()

    def jge(self, lbl):
        self.jmp(lbl) if self.flags['zf'] or not self.flags['sf'] else self.__increment_instruction_pointer__()

    def jg(self, lbl):
        self.jmp(lbl) if not self.flags['zf'] and not self.flags['sf'] else self.__increment_instruction_pointer__()

    def jle(self, lbl):
        self.jmp(lbl) if self.flags['zf'] or self.flags['sf'] else self.__increment_instruction_pointer__()

    def jl(self, lbl):
        self.jmp(lbl) if not self.flags['zf'] and self.flags['sf'] else self.__increment_instruction_pointer__()

    def call(self, lbl):
        # set link register to address to return to after ret
        self.regs['lr'] = self.regs['ip'] + 1
        self.jmp(lbl)

    def ret(self):
        self.regs['ip'] = self.regs['lr']

    def msg(self, *args):
        print(*args)
        self.__increment_instruction_pointer__()

    def end(self):
        # figure this out last
        self.__increment_instruction_pointer__()

    def run(self, code):
        while self.regs['ip'] < len(code):
            line = code[self.regs['ip']]
            instruction = line[0]
            args = line[1:]
            print("ins: {}, args: {}".format(instruction, args))
            self.instructions[instruction](*args)
            print("regs: {}".format(self.regs))


def assembler_interpreter(program):
    interpreter = Interpreter()
    code = interpreter.__preprocess__(program)
    return interpreter.run(code)


if __name__ == '__main__':
    program = program = """
    ; My first program
    mov  a, 5
    inc  a
    call function
    msg  '(5+1)/2 = ', a    ; output message
    end

    function:
        div  a, 2
        ret
    """
    assembler_interpreter(program)
