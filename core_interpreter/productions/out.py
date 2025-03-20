import core_interpreter.productions.id_list as idlist

import core_interpreter.config as config

class Out:
    def __init__(self):
        self.id_list = None

    def parse_out(self):
        config.TOKENIZER.skipToken() #write

        self.id_list = idlist.IdList()
        self.id_list.parse_id_list()

        config.TOKENIZER.skipToken() #;

    def print_out(self):
        print('write ', end='')
        self.id_list.print_id_list()
        print(';')

    def exec_out(self):
        self.id_list.print_id_list(verbose=True) #verbose writes ids w/ values like: X = 25