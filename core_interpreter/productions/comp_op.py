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

    def parse_comp_op(self):
        op_str = config.TOKENIZER.getToken()[1]
        assert op_str in CompOp.ops
        self.alt_no = CompOp.ops[op_str]