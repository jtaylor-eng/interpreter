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

    def print_in(self, indent):
        print('\t' * indent, end='')
        print('read ', end='')
        self.id_list.print_id_list()
        print(';')

    def eval_in(self):
        try:
            ids = self.id_list.exec_id_list()
            for id in ids:
                id.val = config.INPUTS.pop(0)
        except:
            print(f'Error: Expected input from data_file, but none was found.')
            exit()