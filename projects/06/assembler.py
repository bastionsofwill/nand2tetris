import parser
import decoder
import symboltable
from enum import Enum

class CmdType(Enum):
    A_INSTRUCTION = 0
    C_INSTRUCTION = 1
    L_INSTRUCTION = 2
    
filename = 'test.txt'
f = open(filename, 'r', encoding="utf-8")

p = parser.Parser(f)
while(p.has_more_commands()):
    print(p.cmd_now)
    p.advance()