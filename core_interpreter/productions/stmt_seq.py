import core_interpreter.productions.stmt as stmt

import core_interpreter.config as config

class StmtSeq:
    def __init__(self):
        #<stmt seq>	::= <stmt> | <stmt> <stmt seq>
        self.stmt = None
        self.ss = None

    def parse_stmt_seq(self):
        self.stmt = stmt.Stmt()
        self.stmt.parse_stmt()

        next_tok = config.TOKENIZER.getToken()[1]
        if next_tok in ['if', 'while', 'read', 'write'] or \
           next_tok.isupper(): #is Id
            self.ss = StmtSeq()
            self.ss.parse_stmt_seq()
        
    def print_stmt_seq(self):
        self.stmt.print_stmt()

        if self.ss is not None:
            self.ss.print_stmt_seq()

    def exec_stmt_seq(self):
        self.stmt.exec_stmt()

        if self.ss is not None:
            self.ss.exec_stmt_seq()