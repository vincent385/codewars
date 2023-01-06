class Message:
    def __init__(self, text, registers):
        self.__text = text
        self.__regs = registers

    def process(self):
        def advance():
            self.__index += 1
            self.__current_char = self.__text[self.__index] if self.__index < len(self.__text) else None

        def read_raw_text():
            text = ""
            while self.__current_char != "'":
                text += self.__current_char
                advance()
            advance()
            return text

        lalphabet = 'abcdefghijklmnopqrstuvwxyz'
        string = ''
        self.__index = 0
        self.__current_char = self.__text[self.__index]
        while self.__current_char != None:
            if self.__current_char == "'":
                advance()
                string += read_raw_text()
            elif self.__current_char in lalphabet:
                string += str(self.__regs[self.__current_char])
                advance()
            advance()
        self.out = string


class Interpreter:
    def __init__(self):
        self.regs = {
            'ip': 0,
            'lr': 0,
            'out': ''
        }
        self.flags = {
            'zf': False,
            'sf': False,
            'ex': False
        }
        self.first_label_idx = None
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
                    if not self.first_label_idx:
                        self.first_label_idx = idx + 1
            else:
                lines.pop(idx)
                idx -= 1
            idx += 1
        return lines

    def __increment_instruction_pointer__(self):
        self.regs['ip'] += 1

    def get_value(self, val):
        return self.regs[val] if val in self.regs else int(val)

    def mov(self, x, y):
        x = x.replace(',', '')
        self.regs[x] = self.get_value(y)
        self.__increment_instruction_pointer__()

    def inc(self, x):
        self.regs[x] += 1
        self.__increment_instruction_pointer__()

    def dec(self, x):
        self.regs[x] -= 1
        self.__increment_instruction_pointer__()

    def add(self, x, y):
        x = x.replace(',', '')
        self.regs[x] += self.get_value(y)
        self.__increment_instruction_pointer__()

    def sub(self, x, y):
        x = x.replace(',', '')
        self.regs[x] -= self.get_value(y)
        self.__increment_instruction_pointer__()

    def mul(self, x, y):
        x = x.replace(',', '')
        self.regs[x] *= self.get_value(y)
        self.__increment_instruction_pointer__()

    def div(self, x, y):
        x = x.replace(',', '')
        self.regs[x] //= self.get_value(y)
        self.__increment_instruction_pointer__()

    def jmp(self, lbl):
        self.regs['ip'] = self.labels[lbl]

    def cmp(self, x, y):
        x = x.replace(',', '')
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
        if self.regs['ip'] < self.first_label_idx: self.regs['lr'] = self.regs['ip'] + 1
        self.jmp(lbl)

    def ret(self):
        self.regs['ip'] = self.regs['lr']

    def msg(self, *args):
        message = Message(" ".join(args), self.regs)
        message.process()
        self.regs['out'] = message.out
        self.__increment_instruction_pointer__()

    def end(self):
        self.regs['ip'] = len(self.code)
        self.flags['ex'] = True

    def run(self, code, debug=False):
        self.code = code
        while self.regs['ip'] < len(self.code):
            line = self.code[self.regs['ip']]
            instruction = line[0]
            args = line[1:]
            if debug:
                print(f'instruction: {instruction}, args: {args}')
                print(f'labels: {self.labels}')
                print(f'regs: {self.regs}\n')
            self.instructions[instruction](*args)
        if not self.flags['ex']:
            return -1
        return self.regs['out']


def assembler_interpreter(program):
    interpreter = Interpreter()
    code = interpreter.__preprocess__(program)
    return interpreter.run(code, False)
