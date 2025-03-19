import core_interpreter.productions.assign as assign
import core_interpreter.productions.ifCORE as _if
import core_interpreter.productions.loop as loop
import core_interpreter.productions.inCORE as _in
import core_interpreter.productions.out as out

import core_interpreter.config as config

class Stmt:
    def __init__(self):
        self.alt_no = 0

        self.assign = None
        self._if = None
        self.loop = None
        self._in = None
        self.out = None

    def parse_stmt(self):
        tok = config.TOKENIZER.getToken()
        tok_no = tok[0]

        if tok_no == 32:
            self.alt_no = 1
            self.assign = assign.Assign()
            self.assign.parse_assign()
        elif tok_no == 5:
            self.alt_no = 2
            self._if = _if.If()
            self._if.parse_if()
        elif tok_no == 9:
            self.alt_no = 3
            self.loop = loop.Loop()
            self.loop.parse_loop()
        elif tok_no == 10:
            self.alt_no = 4
            self._in = _in.In()
            self._in.parse_in()
        elif tok_no == 11:
            self.alt_no = 5
            self.out = out.Out()
            self.out.parse_out()

    def print_stmt(self):
        if self.alt_no == 1:
            self.assign.print_assign()
        elif self.alt_no == 2:
            self._if.print_if()
        elif self.alt_no == 3:
            self.loop.print_loop()      
        elif self.alt_no == 4:
            self._in.print_in()
        elif self.alt_no == 5:
            self.out.print_out()
        else:
            print('debug', self.alt_no)

    def exec_stmt(self):
        if self.alt_no == 1:
            self.assign.exec_assign()
        elif self.alt_no == 2:
            self._if.exec_if()
        elif self.alt_no == 3:
            self.loop.exec_loop()      
        elif self.alt_no == 4:
            self._in.exec_in()
        elif self.alt_no == 5:
            self.out.exec_out()