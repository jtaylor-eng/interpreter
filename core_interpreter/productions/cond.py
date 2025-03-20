import core_interpreter.productions.comp as comp

import core_interpreter.config as config

class Cond:
    def __init__(self):
        self.comp = None
        self.alt_no = -1

        self.cond1 = None
        self.cond2 = None

    def parse_cond(self):
        first_token = config.TOKENIZER.getToken()[1]

        if first_token == '(':
            self.alt_no = 1
            self.comp = comp.Comp()
            self.comp.parse_comp()


        elif first_token == '!':
            self.alt_no = 2
            config.TOKENIZER.skipToken()
            
            self.cond1 = Cond()
            self.cond1.parse_cond()

        else: #production rule must be [<cond> && <cond] or [<cond> || <cond>]
            assert first_token == '['
            config.TOKENIZER.skipToken() #opening [
           
            #parse cond1
            self.cond1 = Cond()
            self.cond1.parse_cond()

            #handle && or ||
            op_tok = config.TOKENIZER.getToken()[1]
            self.alt_no = 3 if op_tok == '&&' else 4
            config.TOKENIZER.skipToken() # && or ||

            #parse cond2
            self.cond2 = Cond()
            self.cond2.parse_cond()
            
            config.TOKENIZER.skipToken() #closing ]

    def print_cond(self):
        if self.alt_no == 1:
            self.comp.print_comp()
        elif self.alt_no == 2:
            print('!', end='')
            self.cond1.print_cond()
        else:
            print('[', end='')
            self.cond1.print_cond()

            if self.alt_no == 3: print(' && ', end='')
            else: print(' || ', end='')

            self.cond2.print_cond()
            print(']')
    
    def eval_cond(self):
        if self.alt_no == 1:
            return self.comp.eval_comp()
        elif self.alt_no == 2:
            return not self.cond1.eval_cond()
        elif self.alt_no == 3:
            return self.cond1.eval_cond() and self.cond2.eval_cond()
    
        return self.cond1.eval_cond() or self.cond2.eval_cond()
