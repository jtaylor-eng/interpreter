import core_interpreter.productions.int as _int
import core_interpreter.productions.id as id
import core_interpreter.productions.exp as exp

import core_interpreter.config as config

class Op:
    def __init__(self):
        self.int = None
        self.id = None
        self.exp = None
        self.alt_no = 0

    def parse_op(self):
        first_tok = config.TOKENIZER.getToken()[1]

        if first_tok.isnumeric():
            self.alt_no = 1
            self.int = _int.Int()

            self.int.parse_int()

        elif first_tok[0] == '(':
            config.TOKENIZER.skipToken() #open paren
            self.alt_no = 3
            self.exp = exp.Exp()

            self.exp.parse_exp()

            config.TOKENIZER.skipToken() #close paren

        else:
            self.alt_no = 2
            self.id = id.Id.parse_id()

    def print_op(self):
        if self.alt_no == 1:
            self.int.print_int()
        elif self.alt_no == 2:
            self.id.print_id()
        else:
            print('(', end='')
            self.exp.print_exp()
            print(')')

    def eval_op(self):
        if self.alt_no == 1:
            return self.int.eval_int()
        elif self.alt_no == 2:
            return self.id.val
        else:
            return self.exp.eval_exp()