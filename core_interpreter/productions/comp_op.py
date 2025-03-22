import core_interpreter.config as config

class CompOp:
    ops = {
        '!=': 1,
        '==': 2,
        '<' : 3,
        '>' : 4,
        '<=': 5,
        '>=': 6,        
    }

    def __init__(self):
        self.alt_no = -1
        self.op_str = 'invalid'

    def parse_comp_op(self):
        self.op_str = config.TOKENIZER.getToken()[1]
        self.alt_no = CompOp.ops[self.op_str]

        config.assert_proper_token(CompOp.ops.keys(), 'comp_op')
        config.TOKENIZER.skipToken() #skip operator

    def print_comp_op(self):
        print(self.op_str, end='')