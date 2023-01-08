# Tokens
ADD = 'TT_ADD'
MINUS = 'TT_MIN'
EQUALS = 'TT_EQ'
VARIABLE = 'TT_VAR'
CONSTANT = 'TT_CONST'


class Token:
    def __init__(self, _type, value=None):
        self.type = _type
        self.value = value

    def __repr__(self):
        return "Token({}: {})".format(self.type, self.value)


# Lexer
class Lexer:
    def __init__(self, equation):
        self.equation = equation
        self.char_idx = 0
        self.current_char = None
        self.advance()

    def make_tokens(self):
        variables = "abcdefghijklmnopqrstuvwxyz"
        numbers = "0123456789"
        tokens = []
        while self.current_char != None:
            if self.current_char == '+':
                tokens.append(Token(ADD))
            elif self.current_char == '-':
                tokens.append(Token(MINUS))
            elif self.current_char == '=':
                tokens.append(Token(EQUALS))
            elif self.current_char in variables:
                tokens.append(Token(VARIABLE, self.current_char))
            elif self.current_char in numbers:
                tokens.append(Token(CONSTANT, self.current_char))
            self.advance()
        return tokens

    def advance(self):
        self.current_char = self.equation[self.char_idx] if self.char_idx < len(self.equation) else None
        self.char_idx += 1


# Parser
class Parser:
    def __init__(self):
        self.token_idx = 0
        self.current_token = None

    def parse(self, tokens):
        self.tokens = tokens
        self.advance()
        while self.current_token != None:
            NotImplemented

    def advance(self):
        self.current_token = self.tokens[self.token_idx] if self.token_idx < len(self.tokens) else None
        self.token_idx += 1


def solve(eq: str):
    lexer = Lexer(eq)
    tokens = lexer.make_tokens()
    # parser = Parser()
    # nodes = parser.parse(tokens)
    print(tokens)


solve('x + 1 = 9 - 2')
