import core_interpreter.productions.id as id

import core_interpreter.config as config

class IdList:
    def __init__(self):
        #<id list>		::=	<id> | <id>, <id list>
        self.id = None
        self.id_list = None

    def parse_id_list(self, decl_mode=False, assign_mode=False):
        first_tok = config.TOKENIZER.getToken()[1]
        self.id = id.Id(name=first_tok)
        self.id = id.Id.parse_id(decl_mode=decl_mode, assign_mode=assign_mode)

        if config.TOKENIZER.getToken()[1] == ',':
            config.TOKENIZER.skipToken()
            self.id_list = IdList()
            self.id_list.parse_id_list(decl_mode=decl_mode, assign_mode=assign_mode)

    def print_id_list(self, verbose=False):
        self.id.print_id(verbose=verbose)
        
        if self.id_list is not None:
            if not verbose: print(', ', end='') #use commas to delimate in pretty print, new line otherwise
            self.id_list.print_id_list(verbose=verbose)

    def exec_id_list(self):
        #parsing id list should declare all the ids by the Id.parse_id() static method
        # print(self.id, self.id_list)
        if self.id_list is not None:
            ls = [self.id]
            ls.extend(self.id_list.exec_id_list())
            return ls
        
        return [self.id]
