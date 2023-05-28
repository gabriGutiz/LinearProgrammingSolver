
import sys

sys.path.append('./LinProgSolver/utils')

from LinProgInterpreter import Lexer

def main():
    val = 'const: test + 123 >= true or false = akd'
    lex = Lexer(val)
    res = lex.lex()
    print('[')
    for i in res:
        print(f'\t{i},')
    print(']')
    
if __name__ == '__main__':
    main()
