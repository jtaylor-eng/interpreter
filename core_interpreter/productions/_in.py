import core_interpreter.productions.id_list as idlist

import core_interpreter.config as config

class In:
    def __init__(self):
        self.id_list = None

    def parse_in(self):
        config.TOKENIZER.skipToken() #read

        self.id_list = idlist.IdList()
        self.id_list.parse_id_list()

        config.TOKENIZER.skipToken() #;

    def print_in(self):
        print('read', end='')
        self.id_list.print_id_list()

    def exec_in(self):
        raise NotImplementedError