import sys # for cli args

#tokenizer class from proj. 1
from core_interpreter.tokenizer.tokenizer import TokenizerCORE

#global variable to use the tokenizer objext in production classes found in productions/
import core_interpreter.config as config

#individual classes for each production in BNF, all include parse,print,exec
from core_interpreter.productions.comp_op import CompOp
from core_interpreter.productions.comp import Comp
from core_interpreter.productions.prog import Prog
from core_interpreter.productions.id import Id
from core_interpreter.productions.out import Out
from core_interpreter.productions.stmt import Stmt
from core_interpreter.productions.stmt_seq import StmtSeq
from core_interpreter.productions._in import In
from core_interpreter.productions.cond import Cond
from core_interpreter.productions.op import Op
from core_interpreter.productions.decl_seq import DeclSeq
from core_interpreter.productions.assign import Assign
from core_interpreter.productions.loop import Loop
from core_interpreter.productions.fac import Fac
from core_interpreter.productions.decl import Decl
from core_interpreter.productions.exp import Exp
from core_interpreter.productions.int import Int
from core_interpreter.productions.id_list import IdList
from core_interpreter.productions._if import If

def main():
    assert len(sys.argv) == 3
    program_file = sys.argv[1]
    data_file = sys.argv[2]

    #init scanner/tokenizer object from command line argument
    config.TOKENIZER = TokenizerCORE(program_file=program_file)

    program_parser = Prog()

    print("Beginning Parsing:")
    program_parser.parse_prog()

    print("Pretty Printing Program:")
    program_parser.print_prog()

    print("Executing Program:")
    program_parser.exec_prog()

if __name__ == '__main__':
    main()