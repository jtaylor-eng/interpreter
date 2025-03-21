import core_interpreter.productions.cond as cond
import core_interpreter.productions.stmt_seq as stmtseq

import core_interpreter.config as config

class Loop:
    def __init__(self):
        self.cond = None
        self.ss = None

    def parse_loop(self):
        config.TOKENIZER.skipToken() #while tok

        self.cond = cond.Cond() #parse while cond
        self.cond.parse_cond()

        config.TOKENIZER.skipToken() #loop tok

        self.ss = stmtseq.StmtSeq() #parse stmt seq
        self.ss.parse_stmt_seq()

        config.TOKENIZER.skipToken() #end
        config.TOKENIZER.skipToken() #;

    def print_loop(self, indent):
        print('\t' * indent, end='')
        print('while ', end='')
        self.cond.print_cond()
        print(' loop')
        self.ss.print_stmt_seq(indent=indent+1)
        print('\t' * indent, end='')
        print('end;')

    def exec_loop(self):
        while self.cond.eval_cond():
            self.ss.exec_stmt_seq()
