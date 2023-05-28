
from enum import Enum
import sys

# sys.path.append("../../LinProgSolver")

# from LinProgProblemException import LinProgProblemException

class Definition(Enum):
    CONSTRAINT = 'constr'
    OBJ_FUNC = 'obj'

class Operators(Enum):
    SUM = '+'
    SUB = '-'
    DIV = '/'
    TIMES = '*'
    ELV = '^'
    AND = 'and'
    OR = 'or'
    TRUE = 'true'
    FALSE = 'false'

class Comparison(Enum):
    BIGGER = '>'
    SMALLER = '<'
    EQUALS = '='
    BIGGER_EQ = '>='
    SMALLER_EQ = '<='

class Type(Enum):
    COMPARISON = Comparison
    DEFINITION = Definition
    OPERATORS = Operators
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

class Lexer:

    input: str
    size: int

    def __init__(self, input_code: str):
        inp = input_code.strip().lower()
        self.input = inp
        self.size = len(inp)

    def __continue_searching(self, inp: str) -> bool:
        return (inp.isalnum() or (inp in Token.search))

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
                text = ""
                token = None
                while current_pos < self.size and self.__continue_searching(val):
                    text += self.input[current_pos]

                    verif = False
                    for tpe in (Type):
                        print(tpe)
                        if tpe == Type.NUMERIC or tpe == Type.IDENTIFIER:
                            continue
                        if text in (tpe.value):
                            token = tpe.value(text)
                            verif = True
                            break
                    if verif:
                        break

                    current_pos += 1
                if not token:
                    if text.isnumeric():
                        token = Type.NUMERIC
                    else:
                        token = Type.IDENTIFIER
                tokens.append(Token(token, text, token_pos))

            else:
                # raise LinProgProblemException(f"Unknown token {text} at {current_pos}")
                print(f"Unknown token {text} at {current_pos}")
                return []
        return tokens

class LinProgInterpreter:
    pass
