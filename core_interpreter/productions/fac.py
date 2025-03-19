import core_interpreter.productions.op as op

import core_interpreter.config as config

class Fac:
    def __init__(self):
        self.op  = None
        self.fac = None
        self.alt_no = 1 #by default, assume no *

    def parse_fac(self):
        self.op = op.Op()
        self.op.parse_op()

        if config.TOKENIZER.getToken()[1] == '*':
            config.TOKENIZER.skipToken()
            self.fac = Fac()
            self.fac.parse_fac()
            self.alt_no = 2

    def print_fac(self):
        self.op.print_op()

        if self.alt_no == 2:
            print(' * ', end='')
            self.fac.print_fac()

    def eval_fac(self):
        if self.alt_no == 1:
            return self.op.eval_op()
        
        return self.op.eval_op() * self.fac.eval_fac()