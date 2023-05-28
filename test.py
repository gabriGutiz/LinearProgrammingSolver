
import sys

sys.path.append('./LinProgSolver/utils')

from LinProgInterpreter import Lexer

def print_output(res: list) -> None:
    print('[')
    for i in res:
        print(f'\t{i},')
    print(']')

def main():
    val = 'const: test + 123 >= true or false = akd'
    lex = Lexer(val)
    print_output(lex.lex())

    val = 'constr: test + 123 >= true or false = akd'
    lex = Lexer(val)
    print_output(lex.lex())
    
if __name__ == '__main__':
    main()
