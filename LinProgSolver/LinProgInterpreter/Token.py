from enum import Enum

class Type(Enum):
    CONSTRAINT = 'constr:'
    OBJ_FUNC = 'obj:'
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
