class Coder:
    def dest(self, d):
        d1 = '0'
        d2 = '0'
        d3 = '0'
        if "A" in d:
            d1 = '1'
        if "D" in d:
            d2 = '1'
        if "M" in d:
            d3 = '1'
        return f"{d1}{d2}{d3}"
    
    def comp(self, c):
        a = '0'
        c1 = '0'
        c2 = '0'
        c3 = '0'
        c4 = '0'
        c5 = '0'
        c6 = '0'
        if "M" in c: # A or M
            a = '1'
        temp = c.replace("M", "A")
        if "D" not in temp: # zx
            c1 = '1'
        if temp in ["1", "-1", "A", "!A", "-A", "D+1", "A+1", "A-1", "D-A", "D|A"]: # nx
            c2 = '1'
        if "A" not in temp: # zy
            c3 = '1'
        if temp in["1", "D", "!D", "-D", "D+1", "A+1", "D-1", "A-D", "D|A"]: # ny
            c4 = '1'
        if temp in["0", "1", "-1", "-D", "-A", "D+1", "A+1", "D-1", "A-1", "D+A", "D-A", "A-D"]: # f
            c5 = '1'
        if temp in["1", "!D", "!A", "-D", "-A", "D+1", "A+1", "D-A", "A-D", "D|A"]: # no
            c6 = '1'
        return f"{a}{c1}{c2}{c3}{c4}{c5}{c6}"
    
    def jump(self, j):
        j1 = '0'
        j2 = '0'
        j3 = '0'
        if j in ["JLT", "JNE", "JLE", "JMP"]:
            j1 = '1'
        if j in ["JEQ", "JGE", "JLE", "JMP"]:
            j2 = '1'
        if j in ["JGT", "JGE", "JNE", "JMP"]:
            j3 = '1'
        return f"{j1}{j2}{j3}"