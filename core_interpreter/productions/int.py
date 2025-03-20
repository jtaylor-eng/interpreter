import core_interpreter.config as config

class Int:
    def __init__(self):
        self.val = 0

    def parse_int(self):
        self.val = int(config.TOKENIZER.getToken()[1])
        config.TOKENIZER.skipToken()

    def print_int(self):
        print(self.val, end='')
    
    def eval_int(self):
        return self.val