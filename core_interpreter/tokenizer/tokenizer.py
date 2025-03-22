import sys
from typing import List, Tuple

class TokenizerCORE:
    RESERVED = {
        'program': 1,
        'begin': 2,
        'end': 3,
        'int': 4,
        'if': 5,
        'then': 6,
        'else': 7,
        'while': 8,
        'loop': 9,
        'read': 10,
        'write': 11
    }

    SPECIAL = {
        ';': 12,
        ',': 13,
        '=': 14,
        '!': 15,
        '[': 16,
        ']': 17,
        '&&': 18,
        '||': 19,
        '(': 20,
        ')': 21,
        '+': 22,
        '-': 23,
        '*': 24,
        '!=': 25,
        '==': 26,
        '<': 27,
        '>': 28,
        '<=': 29,
        '>=': 30
    }

    SPECIAL_CHARS = set(''.join(list(SPECIAL.keys()))) #set of special characters (i.e. '&' not '&&') -- to be used in __getToken()

    EOF_CODE = 33
    ERROR_CODE = 34

    def __init__(self, program_file: str, verbose=False):
        """Constructor for Tokenizer. Takes program file name as input.

        Args:
            program_file (str):  name of the input file that
            contains the string of characters to be tokenized

            verbose: whether to print the tokens found in file
        """
        self._tokens: List[Tuple[int, str]] = []

        self.verbose = verbose

        with open(program_file, 'r') as fp:
            self.cursor_index = 0
            self._file_contents = fp.read()
            self._file_lines = self._file_contents.split('\n')

            self.__tokenizeLine()

            self.cursor_index = 0 # set the cursor to 0 as specified in proj. desc.
    
    def getToken(self):
        return self._tokens[self.cursor_index]

    def skipToken(self):
        self.cursor_index += 1

    def __tokenizeLine(self):
        self._curr_line = ''

        # ignore whitespace until line with content found
        while self._file_lines and len(self._curr_line) == 0:
            self._curr_line = self._file_lines.pop(0)
            self._curr_line = self._curr_line.lstrip()

        # continually process tokens according to line
        while True:
            if len(self._tokens) > 0 and self._tokens[-1][0] in {self.EOF_CODE, self.ERROR_CODE}:
                return
        
            ret_tok = self.__getToken()

            if self.verbose:
                print(f'Returned token: {ret_tok}')
            if self.verbose and ret_tok[0] in {self.EOF_CODE, self.ERROR_CODE}:
                print(f'Token id of {ret_tok[0]} reached, terminating.')
            
            self._tokens.append(ret_tok)
            self.__skipToken()

    def __getToken(self):
        if len(self._curr_line) == 0: # at EOF
            return (self.EOF_CODE, 'EOF')
        
        elif self._curr_line[0].islower(): #reserved keyword must start with lower
            return self.__process_reserved(self._curr_line)
        
        elif self._curr_line[0] in self.SPECIAL_CHARS: #special keyword starts with alphabet {self.SPECIAL_CHARS}
            return self.__process_special(self._curr_line)
        
        elif self._curr_line[0].isnumeric(): #ints must start with numeric char of course
            return self.__process_integer(self._curr_line)
        
        elif self._curr_line[0].isupper(): #id name must start with uppercase char
            return self.__process_id(self._curr_line)
        
        #token not accepted by DFA, probably caught by now, but just in case
        return (self.ERROR_CODE, 'ERR') 
        
    def __skipToken(self):
        if self._tokens[-1][0] in {self.EOF_CODE, self.ERROR_CODE}: # return early if EOF or ERR
            return
        
        self.cursor_index += 1            

        curr_tok = self.__getToken()

        self._curr_line = self._curr_line[len(curr_tok[1]):].lstrip()

        if len(self._curr_line) == 0: # continue tokenizing file if line empty
            self.__tokenizeLine()

    """
    intVal and idName not needed for Tokenizer functionality, but will be used in parser.
    Luckily, I am storing tokens ids with their string values.
    """
    def intVal(self) -> int:
        return int(self._tokens[self.cursor_index][1])

    def idName(self) -> str:
        return self._tokens[self.cursor_index][1]
    
    """
    The following 4 private methods are used to process reserved, special, int, and id tokens respectively.
    """
    def __process_reserved(self, line: str):
        # tok starts with lower, must be reserved word
        for reserved_word, token in self.RESERVED.items():
            if line.startswith(reserved_word):
                return (token, reserved_word)

        return (self.ERROR_CODE, 'ERR')

    def __process_special(self, line: str):
        # sort self.SPECIAL to include longest first. This will ensure greedy decoding is used
        for special_word in sorted(self.SPECIAL.keys(), key=len, reverse=True):
            if line.startswith(special_word):
                return (self.SPECIAL[special_word], special_word)

        return (self.ERROR_CODE, 'ERR')      

    def __process_integer(self, line: str):
        int_len = 0
        line_cp = line

        # we know since __process_integer was called, first char in tok is digit,
        # now we need to determine whether every char in the tok is digit
        while line_cp and line_cp[0].isdigit():
            int_len += 1
            line_cp = line_cp[1:]

        return (31, line[:int_len])

    def __process_id(self, line: str):
        id_len = 0
        line_cp = line

        # we know since __process_id was called, first char in tok is upper,
        # now we need to determine whether every char in the tok is upper or digit
        while line_cp and (line_cp[0].isdigit() or line_cp[0].isupper()):
            id_len += 1
            line_cp = line_cp[1:]

        return (32, line[:id_len])
    
    """
    self._tokens stores (tok id, tok str) pairs. 
    The following properties are used for accessing the pairs, just the ids, or just the strings.
    Also set property for extracting cursor index and original program string. May be convenient for TokenizerCORE user.
    """
    @property
    def tokens(self):
        return self._tokens
    
    @property
    def token_ids(self):
        return [tok[0] for tok in self._tokens]
    
    @property
    def token_strings(self):
        return [tok[1] for tok in self._tokens]
    
    @property
    def program_str(self):
        return self._file_contents


if __name__ == '__main__':
    prog_file = sys.argv[1] # CORE program file passed as command line argument
    tokenizer = TokenizerCORE(program_file=prog_file)

    print(f'\nProgram {prog_file}\'s Tokens Object:\n{tokenizer.tokens}')

    print(f'\nToken IDs:\n{tokenizer.token_ids}')