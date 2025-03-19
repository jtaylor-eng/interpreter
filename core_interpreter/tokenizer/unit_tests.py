import unittest
from tokenizer import TokenizerCORE

class TestTokenizer(unittest.TestCase):
    def test_sample(self):
        file_test = 'tests/sample_prog.txt'
        expected_tok_ids = [1, 4, 32, 12, 2, 32, 14, 31, 12, 11, 32, 12, 3, 33]

        self.assertEqual(TokenizerCORE(file_test).token_ids, expected_tok_ids)

    def test_sample_whitespace(self):
        file_test = 'tests/sample_prog_whitespace.txt'
        expected_tok_ids = [1, 4, 32, 12, 2, 32, 14, 31, 12, 11, 32, 12, 3, 33]

        self.assertEqual(TokenizerCORE(file_test).token_ids, expected_tok_ids)

    def test_greedy(self):
        file_test = 'tests/greedy.txt'
        expected_tok_ids = [26, 26, 12, 30, 29, 25, 14, 26, 14, 33]

        self.assertEqual(TokenizerCORE(file_test).token_ids, expected_tok_ids)

    def test_early_error(self):
        file_test = 'tests/early_error.txt'
        expected_tok_ids = [1, 4, 32, 12, 2, 34]

        self.assertEqual(TokenizerCORE(file_test).token_ids, expected_tok_ids)

    def test_error_full(self):
        file_test = 'tests/error_full.txt'
        expected_tok_ids = [1, 4, 32, 13, 32, 13, 32, 12, 4, 32, 12, 2, 32, 14, 31, 12, 32, 14, 31, 12, 32, 14, 31, 12, 32, 14, 31, 12, 5, 16, 32, 26, 32, 17, 6, 34]

        self.assertEqual(TokenizerCORE(file_test).token_ids, expected_tok_ids)

    def test_full_prog(self):
        file_test = 'tests/full_prog.txt'
        expected_tok_ids = [1, 4, 32, 13, 32, 13, 32, 12, 4, 32, 12, 2, 32, 14, 31, 12, 32, 14, 31, 12, 32, 14, 31, 12, 32, 14, 31, 12, 5, 16, 32, 26, 32, 17, 6, 32, 14, 31, 12, 3, 12, 5, 16, 32, 26, 32, 17, 6, 32, 14, 31, 12, 3, 12, 11, 32, 13, 32, 13, 32, 13, 32, 12, 3, 33]

        self.assertEqual(TokenizerCORE(file_test).token_ids, expected_tok_ids)

    def test_given_prog2(self):
        file_test = 'tests/given_prog2.txt'
        expected_tok_ids = [1, 4, 32, 13, 32, 12, 2, 10, 32, 12, 10, 32, 12, 8, 20, 32, 25, 32, 21, 9, 5, 20, 32, 28, 32, 21, 6, 32, 14, 32, 23, 32, 12, 7, 32, 14, 32, 23, 32, 12, 3, 12, 3, 12, 11, 32, 12, 3, 33]

        self.assertEqual(TokenizerCORE(file_test).token_ids, expected_tok_ids)

    def test_given_prog3(self):
        file_test = 'tests/given_prog3.txt'
        expected_tok_ids = [1, 4, 32, 13, 32, 12, 4, 32, 13, 32, 13, 32, 12, 2, 32, 14, 31, 12, 32, 14, 31, 12, 32, 14, 31, 12, 10, 32, 12, 8, 20, 32, 27, 32, 21, 9, 32, 14, 32, 22, 32, 12, 32, 14, 32, 12, 32, 14, 32, 12, 32, 14, 32, 22, 31, 12, 3, 12, 11, 32, 12, 3, 33]

        self.assertEqual(TokenizerCORE(file_test).token_ids, expected_tok_ids)

if __name__ == '__main__':
    unittest.main()