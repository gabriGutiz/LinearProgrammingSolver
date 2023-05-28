
from enum import Enum
import sys

# sys.path.append("../../LinProgSolver")

# from LinProgProblemException import LinProgProblemException

class Type(Enum):
    CONSTRAINT = 'constr'
    OBJ_FUNC = 'obj'
    SUM = '+'
    SUB = '-'
    DIV = '/'
    TIMES = '*'
    ELV = '^'
    AND = 'and'
    OR = 'or'
    TRUE = 'true'
    FALSE = 'false'
    BIGGER = '>'
    SMALLER = '<'
    EQUALS = '='
    BIGGER_EQ = '>='
    SMALLER_EQ = '<='
    DEFINITION = ':'
    NUMERIC = 0
    IDENTIFIER = 1

class Token:
    tk_type: Type
    text: str
    start_index: int

    search = '><'

    def __init__(self, tpe: Type, txt: str, index: int):
        self.tk_type = tpe
        self.text = txt
        self.start_index = index

    def __str__(self) -> str:
        return f'Token(type: {self.tk_type}, text: "{self.text}", start: {self.start_index})'

class Lexer:

    input: str
    size: int

    def __init__(self, input_code: str):
        inp = input_code.strip().lower()
        self.input = inp
        self.size = len(inp)

    def __continue_searching(self, inp: str) -> bool:
        return (inp.isalnum() or (inp in Token.search) or (not inp.endswith(' ')))

    def lex(self) -> list():
        tokens = []
        current_pos = 0

        while current_pos < self.size:
            token_pos = current_pos
            val = self.input[current_pos]

            if val.isspace():
                current_pos += 1
                continue

            elif self.__continue_searching(val):
                text = val
                token = None
                current_pos += 1
                try:
                    while current_pos < self.size and self.__continue_searching(text):
                        if self.input[current_pos].isspace():
                            break

                        text += self.input[current_pos]

                        for tpe in (Type):
                            # print(tpe)
                            if tpe == Type.NUMERIC or tpe == Type.IDENTIFIER:
                                continue
                            if text == tpe.value:
                                token = tpe
                                raise StopIteration()
                        current_pos += 1

                except StopIteration:
                    pass
                finally:
                    if not token:
                        if text.isnumeric():
                            token = Type.NUMERIC
                        else:
                            token = Type.IDENTIFIER
                    tokens.append(Token(token, text, token_pos))
                    current_pos += 1

            else:
                # raise LinProgProblemException(f"Unknown token {text} at {current_pos}")
                print(f"Unknown token {text} at {current_pos}")
                return []
        return tokens

class LinProgInterpreter:
    pass
