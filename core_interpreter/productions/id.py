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
    def parse_id():
        tok_name = config.TOKENIZER.getToken()[1]

        for id in Id.eIds:
            if id.name == tok_name:
                return id

        nId = Id(tok_name)
        Id.eIds.append(nId)

        return nId

    #val, name getters and setters
    #available with .val data member

    def print_id(self, verbose=False):
        if not verbose:
            print(self.name, end=' ')
        else:
            print(f'{self.name} = {self.val}')

    def exec_id(self):
        raise NotImplementedError #shouldn't need to call, just incase someone does