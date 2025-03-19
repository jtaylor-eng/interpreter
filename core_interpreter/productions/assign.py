import core_interpreter.productions.id as id
import core_interpreter.productions.exp as exp

import core_interpreter.config as config

class Assign:
    def __init__(self):
        self.id = None
        self.exp = None

    def parse_assign(self):
        self.id = id.Id.parse_id()

        self.exp = exp.Exp()
        self.exp.parse_exp()
 
    def print_assign(self):
        self.id.print_id()
        print(' = ', end='')
        self.exp.print_exp()
        print(';')

    def exec_assign(self):
        self.id.val = self.exp.eval_exp()

        self.id.initialized = True