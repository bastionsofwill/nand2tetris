#!/usr/bin/env python3
import sys
import os.path
asm_path = os.path.split(os.path.abspath(sys.argv[1]))
hack_path = asm_path[0]
hack_name = asm_path[1].split('.')[0]

asm_file = open(sys.argv[1], 'r')
hack_file = open(f'{hack_path}/{hack_name}.hack', 'w')
lines = asm_file.readlines()
line_count = 0
for line in lines:
    asm_line = line.strip().split("//")[0]
    if asm_line:
        if asm_line[0] == '@': # A-command
            constant = int(asm_line[1:])
            a_command = bin(constant)[2:].rjust(16, "0")
            hack_file.write(a_command)
        else:
            dest = ""
            comp = asm_line
            jump = ""
            if ";" in asm_line:
                jump = asm_line.split(";")[1]
                comp = asm_line.split(";")[0]
            if "=" in comp:
                dest = comp.split("=")[0]
                comp = comp.split("=")[1]
            # dest
            d1 = '0'
            d2 = '0'
            d3 = '0'
            if "A" in dest:
                d1 = '1'
            if "D" in dest:
                d2 = '1'
            if "M" in dest:
                d3 = '1'
            # comp
            a = '0'
            c1 = '0'
            c2 = '0'
            c3 = '0'
            c4 = '0'
            c5 = '0'
            c6 = '0'
            if "M" in comp: # A or M
                a = '1'
            temp = comp.replace("M", "A")
            if "D" not in temp: # zx
                c1 = '1'
            if temp in ["1", "-1", "A", "-A", "D+1", "A+1", "A-1", "D-A", "D|A"]: # nx
                c2 = '1'
            if "A" not in temp: # zy
                c3 = '1'
            if temp in["1", "D", "!D", "-D", "D+1", "A+1", "D-1", "A-D", "D|A"]: # ny
                c4 = '1'
            if temp in["0", "1", "-1", "-D", "-A", "D+1", "A+1", "D-1", "A-1", "D+A", "D-A", "A-D"]: # f
                c5 = '1'
            if temp in["1", "!D", "!A", "-D", "-A", "D+1", "A+1", "D-A", "A-D", "D|A"]: # no
                c6 = '1'
            
            # jmp
            j1 = '0'
            j2 = '0'
            j3 = '0'
            if jump in ["JLT", "JNE", "JLE", "JMP"]:
                j1 = '1'
            if jump in ["JEQ", "JGE", "JLE", "JMP"]:
                j2 = '1'
            if jump in ["JGT", "JGE", "JNE", "JMP"]:
                j3 = '1'
            hack_file.write(f'111 {a} {c1}{c2}{c3}{c4}{c5}{c6} {d1}{d2}{d3} {j1}{j2}{j3}')
        hack_file.write("\n")
        line_count += 1
print(line_count)
hack_file.close
asm_file.close
