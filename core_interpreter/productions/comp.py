import core_interpreter.productions.op as op
import core_interpreter.productions.comp_op as compop

import core_interpreter.config as config

class Comp:
    def __init__(self):
        self.op1 = None
        self.op2 = None
        self.comp_op = None

    def parse_comp(self):
        config.TOKENIZER.skipToken() #open parenthesis

        self.op1 = op.Op() #parse op1
        self.op1.parse_op()

        self.comp_op = compop.CompOp() #parse comparison op
        self.comp_op.parse_comp_op()

        self.op2 = op.Op() #parse op2
        self.op2.parse_op()

        config.TOKENIZER.skipToken() #closing paren

    def print_comp(self):
        print('(', end='')
        self.op1.print_op()
        print(' ', end='')
        self.comp_op.print_comp_op()
        print(' ', end='')
        self.op2.print_op()
        print(')', end='')

    def eval_comp(self):
        op1 = self.op1.eval_op()
        op2 = self.op2.eval_op()
        
        assert self.comp_op.alt_no != -1

        if self.comp_op.alt_no == 1:
            return op1 != op2
        elif self.comp_op.alt_no == 2:
            return op1 == op2
        elif self.comp_op.alt_no == 3:
            return op1 < op2
        elif self.comp_op.alt_no == 4:
            return op1 > op2
        elif self.comp_op.alt_no == 5:
            return op1 <= op2

        return op1 >= op2