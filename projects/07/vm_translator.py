#!/usr/bin/env python3
import sys
import os.path
import glob
from vm_parser import Parser
from vm_code_writer import CodeWriter

input_path = sys.argv[1]
input = os.path.split(os.path.abspath(input_path))
parser = {}
if os.path.isfile(input_path):
    input_files = [input_path]
elif os.path.isdir(input_path):
    input_files = glob.glob(f"{input_path}/*.vm")
for input_file in input_files:
    parser[input_file] = Parser(input_file)

output_path = input[0] + '/' + input[1].split('.')[0] + ".asm"
code_writer = CodeWriter(output_path)
code_writer.set_file_name(input[1].split('.')[0])

for input_file in input_files:
    while(parser[input_file].has_more_commands()):
        parser[input_file].advance()
        match parser[input_file].command_type():
            case "C_ARITHMETIC":
                code_writer.write_arithmetic(parser[input_file].arg1()) 
            case "C_PUSH":
                code_writer.write_push_pop("C_PUSH", parser[input_file].arg1(), parser[input_file].arg2())
            case "C_POP":
                code_writer.write_push_pop("C_POP", parser[input_file].arg1(), parser[input_file].arg2())
            case "C_GOTO":
                pass
            case "C_IF":
                pass
            case "C_FUNCTION":
                pass
            case "C_RETURN":
                pass
            case "C_CALL":
                pass
            case _:
                print("unexpected return value from parser.command_type()")
                exit(1)
code_writer.close()