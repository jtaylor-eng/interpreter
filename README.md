# interpreter

# usage:
(considering you at the top level directory)
python3 -m core_interpreter.interpreter program_file input_data

The project source code is found within the core_interpreter directory
(package).

At the top level of this core_interpreter packages there is:
 - interpreter.py: main method for executing interpreter. takes the command line args for the program_file and input_data
 - config.py: Stores global variables (the tokenizer and input data). The globals are initialized to None here, but set to the proper values in the main method of interpreter.py 
 - productions: subpackage containing the production rule classes (OOP approach to interpreter)
 - tokenizer: subpackage containing tokenizer code and test cases
 - __init__.py, __pycache__: needed so python can properly treat directory as package

config.TOKENIZER._tokens[config.TOKENIZER.cursor_index-1]