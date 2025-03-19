import core_interpreter.productions.id_list as idlist

import core_interpreter.config as config

class Decl:
    def __init__(self):
        self.id_list = None

    def parse_decl(self):
        config.TOKENIZER.skipToken() #int

        self.id_list = idlist.IdList()
        self.id_list.parse_id_list()

    def print_decl(self):
        print('int ', end='')
        self.id_list.print_id_list()

    def exec_decl(self):
        self.id_list.exec_id_list()
