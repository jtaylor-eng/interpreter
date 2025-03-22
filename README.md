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

Tests cases for interpreter exist in simpleTestsCoreInterpreter (see simpleTestsCoreInterpreter/README for more info)
Here I've copied each individual running of the cases found in that directory:
**legal programs test cases:**
python3 -m core_interpreter.interpreter simpleTestsCoreInterpreter/programs/legal/printX.core simpleTestsCoreInterpreter/input/blank.txt
python3 -m core_interpreter.interpreter simpleTestsCoreInterpreter/programs/legal/printXOL.core simpleTestsCoreInterpreter/input/blank.txt

python3 -m core_interpreter.interpreter simpleTestsCoreInterpreter/programs/legal/readPrintX.core simpleTestsCoreInterpreter/input/x.txt

python3 -m core_interpreter.interpreter simpleTestsCoreInterpreter/programs/legal/mathOp.core simpleTestsCoreInterpreter/input/mathOp0N.txt
python3 -m core_interpreter.interpreter simpleTestsCoreInterpreter/programs/legal/mathOp.core simpleTestsCoreInterpreter/input/mathOp0P.txt
python3 -m core_interpreter.interpreter simpleTestsCoreInterpreter/programs/legal/mathOp.core simpleTestsCoreInterpreter/input/mathOp1N.txt
python3 -m core_interpreter.interpreter simpleTestsCoreInterpreter/programs/legal/mathOp.core simpleTestsCoreInterpreter/input/mathOp1P.txt
python3 -m core_interpreter.interpreter simpleTestsCoreInterpreter/programs/legal/mathOp.core simpleTestsCoreInterpreter/input/mathOp2N.txt
python3 -m core_interpreter.interpreter simpleTestsCoreInterpreter/programs/legal/mathOp.core simpleTestsCoreInterpreter/input/mathOp2P.txt
python3 -m core_interpreter.interpreter simpleTestsCoreInterpreter/programs/legal/mathOp.core simpleTestsCoreInterpreter/input/mathOpYgtX.txt

**illegal programs test cases:**
python3 -m core_interpreter.interpreter simpleTestsCoreInterpreter/programs/illegal/PrintXRB.core simpleTestsCoreInterpreter/input/blank.txt

python3 -m core_interpreter.interpreter simpleTestsCoreInterpreter/programs/illegal/PrintXDD1.core simpleTestsCoreInterpreter/input/blank.txt
python3 -m core_interpreter.interpreter simpleTestsCoreInterpreter/programs/illegal/PrintXDD2.core simpleTestsCoreInterpreter/input/blank.txt
python3 -m core_interpreter.interpreter simpleTestsCoreInterpreter/programs/illegal/PrintXUD.core simpleTestsCoreInterpreter/input/blank.txt
python3 -m core_interpreter.interpreter simpleTestsCoreInterpreter/programs/illegal/PrintXUI.core simpleTestsCoreInterpreter/input/blank.txt

**Note:**
If you want to run all of these at once run: python3 tests.py.
