import core_interpreter.productions.decl_seq as declseq
import core_interpreter.productions.stmt_seq as stmtseq

import core_interpreter.config as config

class Prog:
    def __init__(self):
        self.ds = None
        self.ss = None

    def parse_prog(self):
        config.assert_proper_token('program', 'prog')
        config.TOKENIZER.skipToken() #program

        self.ds = declseq.DeclSeq() #parse ds
        self.ds.parse_decl_seq()

        config.assert_proper_token('begin', 'prog')
        config.TOKENIZER.skipToken() #begin
        
        self.ss = stmtseq.StmtSeq() #parse ss
        self.ss.parse_stmt_seq()

        config.assert_proper_token('end', 'prog')
        config.TOKENIZER.skipToken() #end

    def print_prog(self):
        print('program')
        self.ds.print_decl_seq(indent=1)
        print('begin')
        self.ss.print_stmt_seq(indent=1)
        print('end')

    def exec_prog(self):
        self.ds.exec_decl_seq()
        self.ss.exec_stmt_seq()
