import core_interpreter.config as config

class Id:
    eIds = []
    id_count = 0

    def __init__(self, name):
        self.name = name
        self.val = None
        self.declared = True #can init to true since we create Id ad-hoc
        self.initialized = False
        
    @staticmethod
    def parse_id(decl_mode=False, assign_mode=False):
        tok_name = config.TOKENIZER.getToken()[1]
        config.TOKENIZER.skipToken()

        #double declaration
        if decl_mode and tok_name in [id.name for id in Id.eIds]:
            print(f'Error: double declaration on token {tok_name}.')
            exit()

        #undeclared
        if not decl_mode and tok_name not in [id.name for id in Id.eIds]:
            print(f'Error: Id {tok_name} never declared.')
            exit()

        #id already exists, return it
        for id in Id.eIds:
            if id.name == tok_name:
                if not assign_mode and not id.initialized:
                    print(f'Error: Id {tok_name} accessed before initialization.')
                    exit()

                id.initialized = True
                return id

        #id doesn't exist, declare it
        nId = Id(tok_name)
        Id.eIds.append(nId)

        return nId

    #val, name getters and setters
    #available with .val data member

    def print_id(self, verbose=False):
        if not verbose:
            print(self.name, end='')
        else:
            print(f'{self.name} = {self.val}')

    def exec_id(self):
        raise NotImplementedError #shouldn't need to call, just incase someone does