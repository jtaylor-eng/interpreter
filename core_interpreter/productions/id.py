import core_interpreter.config as config

class GenericError(Exception):
    def __init__(self, message):
        self._message = message

    def __str__(self):
        return f'ERROR in program: {self._message}'

class Id:
    eIds = []
    id_count = 0

    DOUBLE_DECL_ERR = 'Id {} was double declared.'
    NOT_INIT_ERR = 'Id {} was not initialized in declaration sequence.'

    def __init__(self, name):
        self.name = name
        self.val = None
        self.declared = True #can init to true since we create Id ad-hoc
        self.initialized = False
        
    @staticmethod
    def parse_id():
        tok_name = config.TOKENIZER.getToken()[1]
        config.TOKENIZER.skipToken()

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
            print(self.name, end='')
        else:
            print(f'{self.name} = {self.val}')

    def exec_id(self):
        raise NotImplementedError #shouldn't need to call, just incase someone does