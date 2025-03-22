import core_interpreter.productions.fac as fac

import core_interpreter.config as config

class Exp:
    def __init__(self):
        self.fac = None
        self.exp = None
        self.alt_no = 1 #by default assume prod rule is just <fac>

    def parse_exp(self):
        self.fac = fac.Fac()
        self.fac.parse_fac()

        next_tok = config.TOKENIZER.getToken()[1]
        if next_tok in ['+', '-']:
            config.assert_proper_token(['+', '-'], 'exp')
            config.TOKENIZER.skipToken() #skip +, -
            self.exp = Exp()
            self.exp.parse_exp()

            self.alt_no = 2 if next_tok == '+' else 3

    def print_exp(self):
        self.fac.print_fac()

        if self.alt_no == 2:
            print(' + ', end='')
            self.exp.print_exp()
        elif self.alt_no == 3:
            print(' - ', end='')
            self.exp.print_exp()

    def eval_exp(self):
        if self.alt_no == 1:
            return self.fac.eval_fac()
        elif self.alt_no == 2:
            return self.fac.eval_fac() + self.exp.eval_exp()
        else:
            return self.fac.eval_fac() - self.exp.eval_exp()