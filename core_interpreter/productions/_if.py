import core_interpreter.productions.cond as cond
import core_interpreter.productions.stmt_seq as stmtseq

import core_interpreter.config as config

class If:
    def __init__(self):
        self.c = None
        self.ss1 = None
        self.ss2 = None

    def parse_if(self):
        config.TOKENIZER.skipToken() #parse condition
        self.c = cond.Cond()
        self.c.parse_cond()

        config.TOKENIZER.skipToken() #parse first ss1 which is certainly present
        self.ss1 = stmtseq.StmtSeq()
        self.ss1.parse_stmt_seq()

        tokNo = config.TOKENIZER.getToken() 
        if tokNo[0] == 3: #production rule #1 (no else)
            config.TOKENIZER.skipToken()
            config.TOKENIZER.skipToken()
            return
        
        config.TOKENIZER.skipToken() #production rule #2 (else branch)
        self.ss2 = stmtseq.StmtSeq()
        self.ss2.parse_stmt_seq()
        config.TOKENIZER.skipToken()
        config.TOKENIZER.skipToken()

    def print_if(self, indent):
        print('\t' * indent, end='')
        print('if ', end='')

        self.c.print_cond()
        print(' then')
        self.ss1.print_stmt_seq(indent=indent+1)

        if self.ss2 is not None: #ss2 exists, execute it
            print(' else')
            self.ss2.print_stmt_seq(indent=indent+1)
        print('\t' * indent, end='')
        print('end;')

    def exec_if(self):
        if self.c.eval_cond():
            self.ss1.exec_stmt_seq()
            return
        if self.ss2 is not None: #condition false and ss2 exists, execute it
            self.ss2.exec_stmt_seq()