import os

os.system('python3 -m core_interpreter.interpreter simpleTestsCoreInterpreter/programs/legal/printX.core simpleTestsCoreInterpreter/input/blank.txt')
os.system('python3 -m core_interpreter.interpreter simpleTestsCoreInterpreter/programs/legal/printXOL.core simpleTestsCoreInterpreter/input/blank.txt')

os.system('python3 -m core_interpreter.interpreter simpleTestsCoreInterpreter/programs/legal/readPrintX.core simpleTestsCoreInterpreter/input/x.txt')

os.system('python3 -m core_interpreter.interpreter simpleTestsCoreInterpreter/programs/legal/mathOp.core simpleTestsCoreInterpreter/input/mathOp0N.txt')
os.system('python3 -m core_interpreter.interpreter simpleTestsCoreInterpreter/programs/legal/mathOp.core simpleTestsCoreInterpreter/input/mathOp0P.txt')
os.system('python3 -m core_interpreter.interpreter simpleTestsCoreInterpreter/programs/legal/mathOp.core simpleTestsCoreInterpreter/input/mathOp1N.txt')
os.system('python3 -m core_interpreter.interpreter simpleTestsCoreInterpreter/programs/legal/mathOp.core simpleTestsCoreInterpreter/input/mathOp1P.txt')
os.system('python3 -m core_interpreter.interpreter simpleTestsCoreInterpreter/programs/legal/mathOp.core simpleTestsCoreInterpreter/input/mathOp2N.txt')
os.system('python3 -m core_interpreter.interpreter simpleTestsCoreInterpreter/programs/legal/mathOp.core simpleTestsCoreInterpreter/input/mathOp2P.txt')
os.system('python3 -m core_interpreter.interpreter simpleTestsCoreInterpreter/programs/legal/mathOp.core simpleTestsCoreInterpreter/input/mathOpYgtX.txt')

os.system('python3 -m core_interpreter.interpreter simpleTestsCoreInterpreter/programs/illegal/PrintXRB.core simpleTestsCoreInterpreter/input/blank.txt')

os.system('python3 -m core_interpreter.interpreter simpleTestsCoreInterpreter/programs/illegal/PrintXDD1.core simpleTestsCoreInterpreter/input/blank.txt')
os.system('python3 -m core_interpreter.interpreter simpleTestsCoreInterpreter/programs/illegal/PrintXDD2.core simpleTestsCoreInterpreter/input/blank.txt')
os.system('python3 -m core_interpreter.interpreter simpleTestsCoreInterpreter/programs/illegal/PrintXUD.core simpleTestsCoreInterpreter/input/blank.txt')
os.system('python3 -m core_interpreter.interpreter simpleTestsCoreInterpreter/programs/illegal/PrintXUI.core simpleTestsCoreInterpreter/input/blank.txt')