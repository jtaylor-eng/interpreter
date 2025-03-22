import core_interpreter.productions.id_list as idlist

import core_interpreter.config as config

class Out:
    def __init__(self):
        self.id_list = None

    def parse_out(self):
        config.assert_proper_token(['write'], 'out')
        config.TOKENIZER.skipToken() #write

        self.id_list = idlist.IdList()
        self.id_list.parse_id_list()

        config.assert_proper_token(';', 'out')
        config.TOKENIZER.skipToken() #;

    def print_out(self, indent):
        print('\t' * indent, end='')
        print('write ', end='')
        self.id_list.print_id_list()
        print(';')

    def exec_out(self):
        # self.id_list.print_id_list(verbose=True) #verbose writes ids w/ values like: X = 25
        for id in self.id_list.exec_id_list():
            val = id.exec_id()
            print(f'{id.name} = {val}')