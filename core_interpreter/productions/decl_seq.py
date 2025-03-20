import core_interpreter.productions.decl as decl

import core_interpreter.config as config

class DeclSeq:
    def __init__(self):
        self.decl = None
        self.ds = None

    def parse_decl_seq(self):
        self.decl = decl.Decl()
        self.decl.parse_decl()

        if config.TOKENIZER.getToken()[1] == 'int':
            self.ds = DeclSeq()
            self.ds.parse_decl_seq()

    def print_decl_seq(self):
        self.decl.print_decl()

        if self.ds is not None:
            self.ds.print_decl_seq()

        print(';')

    def exec_decl_seq(self):
        self.decl.exec_decl()

        if self.ds is not None:
            self.ds.exec_decl_seq()
