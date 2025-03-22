import sys # for cli args

#tokenizer class from proj. 1
from core_interpreter.tokenizer.tokenizer import TokenizerCORE

#global variable to use the tokenizer objext in production classes found in productions/
import core_interpreter.config as config

#top lvl production rule (initiate parser with Prog class)
from core_interpreter.productions.prog import Prog

def main():
    assert len(sys.argv) == 3

    program_file = sys.argv[1]
    data_file = sys.argv[2]

    #init scanner/tokenizer object from command line argument
    config.TOKENIZER = TokenizerCORE(program_file=program_file)

    #init the inputs from data_file as list of int. used in productions._in
    with open(data_file, 'r') as fp:
        contents = fp.read()
        lines = contents.split('\n')

    config.INPUTS = [int(line) for line in lines if line.strip()]

    program_parser = Prog()

    print(' ===     Beginning Parsing:   ===')
    program_parser.parse_prog()
    print(' ===     Parsing complete!    ===\n')

    print(' === Pretty Printing Program: ===')
    program_parser.print_prog()
    print(' ===     End pretty print.    ===\n')

    print(' ===     Executing Program:   === ')
    program_parser.exec_prog()
    print(' ===     Execution finished.  ===')

if __name__ == '__main__':
    main()