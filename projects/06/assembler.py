#!/usr/bin/env python3
import sys
import os.path
from asm_parser import Parser
from asm_coder import Coder
from asm_symbol_table import SymbolTable

input_path = sys.argv[1]
parser_pre = Parser(input_path)
parser = Parser(input_path)
coder = Coder()
symbol_table = SymbolTable()

input = os.path.split(os.path.abspath(input_path))
output_path = input[0] + '/' + input[1].split('.')[0] + ".hack"

# First pass
while(parser_pre.has_more_lines()):
    parser_pre.advance()
    if parser_pre.instruction_type() in ["A_INSTRUCTION", "C_INSTRUCTION"]:
        parser_pre.output_index += 1
    elif parser_pre.instruction_type() == "L_INSTRUCTION":
        symbol_table.add_entry(parser_pre.symbol(), parser_pre.output_index)
# Second pass
with open(output_path, "w") as output:
    while(parser.has_more_lines()):
        parser.advance() 
        if parser.instruction_type() == "A_INSTRUCTION":
            if symbol_table.contains(parser.symbol()):
                address = symbol_table.get_address(parser.symbol())
            else:
                try:
                    address_dec = int(parser.symbol())
                    address = bin(address_dec)[2:]
                except ValueError:
                    symbol_table.add_entry(parser.symbol())
                    address = symbol_table.get_address(parser.symbol())
            output.write(address.rjust(16, "0"))
        elif parser.instruction_type() == "C_INSTRUCTION":
            comp = coder.comp(parser.comp())
            dest = coder.dest(parser.dest())
            jump = coder.jump(parser.jump())
            output.write(f"111{comp}{dest}{jump}")
        else:
            continue
        output.write("\n")