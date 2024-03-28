class CodeWriter:
    def __init__(self, output_path) -> None:
        self.output = open(output_path, 'w')
        self.static_count = 0

    def set_file_name(self, filename):
        self.file_name = filename
        return

    def write_arithmetic(self, command):
        # pop R13
        self.output.write(f"@SP\n")
        self.output.write(f"M=M-1\n")
        self.output.write(f"A=M\n")
        self.output.write(f"D=M\n")
        self.output.write(f"@R13\n")
        self.output.write(f"M=D\n")
        if command not in ["neg", "not"]:
            # pop R14
            self.output.write(f"@SP\n")
            self.output.write(f"M=M-1\n")
            self.output.write(f"A=M\n")
            self.output.write(f"D=M\n")
            self.output.write(f"@R14\n")
            self.output.write(f"M=D\n")
        match command:
            case "add":
                # self.output.write(f"@R13\n")
                # self.output.write(f"D=M\n")
                # self.output.write(f"@R14\n")
                # self.output.write(f"D=D+M\n")
                self.output.write(f"@R13\n")
                self.output.write(f"D=D+M\n")
            case "sub":
                # self.output.write(f"@R13\n")
                # self.output.write(f"D=M\n")
                # self.output.write(f"@R14\n")
                # self.output.write(f"D=D-M\n")
                self.output.write(f"@R13\n")
                self.output.write(f"D=M-D\n")
            case "neg":
                self.output.write(f"D=-D\n")
            case "eq":
                self.output.write(f"@R13\n")
                self.output.write(f"D=M-D")
                self.output.write(f"@R15\n")
                self.output.write(f"D;JEQ")
            case "gt":
                self.output.write(f"@R13\n")
                self.output.write(f"D=M-D")
                self.output.write(f"@R15\n")
                self.output.write(f"D;JEQ")
            case "lt":
                self.output.write(f"@R13\n")
                self.output.write(f"D=M-D")
                self.output.write(f"@R15\n")
                self.output.write(f"D;JEQ")
            case "and":
                self.output.write(f"@R13\n")
                self.output.write(f"D=D&M\n")
            case "or":
                self.output.write(f"@R13\n")
                self.output.write(f"D=D|M\n")
            case "not":
                self.output.write(f"D=!D\n")
            case _:
                print("unexpected arithmetic command")
                return
        # push D
        self.output.write(f"@SP\n")
        self.output.write(f"A=M\n")
        self.output.write(f"M=D\n")
        self.output.write(f"@SP\n")
        self.output.write(f"M=M+1\n")
        self.output.write("\n")
        return

    def write_push_pop(self, command, segment, index):
        match segment:
            case "constant":
                segment_ref = f"@{index}\n"
            case "local": 
                segment_ref = f"@LCL\n"
            case "argument":
                segment_ref = f"@ARG\n"
            case "this":
                segment_ref = f"@{index}\nD=A\n@THIS\nA=D+M\n"
            case "that":
                segment_ref = f"@{index}\nD=A\n@THAT\nA=D+M\n"
            case "pointer":
                if index == 0:
                    segment_ref = f"@THIS\n"
                elif index == 1:
                    segment_ref = f"@THAT\n"
            case "temp":
                segment_ref = f"@{5 +int(index)}\n"
            case "static":
                segment_ref = f"@{self.file_name}.{self.static_count}\n"
                self.static_count += 1
        match command:
            case "C_PUSH": # R[SP++] = x
                self.output.write(segment_ref)
                self.output.write(f"D=M\n")
                self.output.write(f"@SP\n")
                self.output.write(f"A=M\n")
                self.output.write(f"M=D\n")
                self.output.write(f"@SP\n")
                self.output.write(f"M=M+1\n")
            case "C_POP": # x = R[--SP]
                self.output.write(f"@SP\n")
                self.output.write(f"M=M-1\n")
                self.output.write(f"A=M\n")
                self.output.write(f"D=M\n")
                self.output.write(segment_ref)
                self.output.write(f"M=D\n")
            case _:
                print("unexpected push/pop command")
                return
        return

    def close(self):
        self.output.close()
        return