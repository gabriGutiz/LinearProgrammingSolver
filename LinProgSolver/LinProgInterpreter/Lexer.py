
import sys
from Token import *

# sys.path.append("../../LinProgSolver")

# from LinProgProblemException import LinProgProblemException

class Lexer:

    input: str
    size: int

    def __init__(self, input_code: str):
        inp = input_code.strip().lower()
        self.input = inp
        self.size = len(inp)

    def __continue_searching(self, inp: str) -> bool:
        try:
            test = Type(inp)
            return True
        except ValueError:
            return (inp.isalnum() or
                    (inp in Token.search) or
                    (not inp.endswith(' ')))

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
                while current_pos < self.size-1 and self.__continue_searching(text):
                    current_pos += 1
                    if self.input[current_pos].isspace():
                        break
                    text += self.input[current_pos]

                for tpe in (Type):
                    if tpe == Type.NUMERIC or tpe == Type.IDENTIFIER:
                        continue
                    if text == tpe.value:
                        token = tpe

                if not token:
                    if text.isnumeric():
                        token = Type.NUMERIC
                    else:
                        token = Type.IDENTIFIER
                tokens.append(Token(token, text, token_pos))
                current_pos += 1

            else:
                # TODO: USE LinProgProblemException
                # raise LinProgProblemException(f"Unknown token {text} at {current_pos}")
                raise ValueError(f"Unknown token {text} at {current_pos}")
        return tokens
