TOKENIZER = None
INPUTS = None

def assert_proper_token(valid_tokens: list[str], caller):
    if TOKENIZER.getToken()[1] not in valid_tokens:
        print(f'Error: expected token in {valid_tokens}, but was missing in {caller} production.')
        print(f'Instead found token {TOKENIZER.getToken()}')
        exit()