class CodeWriter:
    def __init__(self, output_path) -> None:
        self.output = open(output_path, 'w')
        self.static_count = 0

    def set_file_name(self, filename):
        self.file_name = filename
        return

    def write_arithmetic(self, command):
        # match command:
        #     case "add":

        #     case "sub":
        #     case "neg":
        #     case "eq":
        #     case "gt":
        #     case "lt":
        #     case "and":
        #     case "or":
        #     case "not":
        #     case _:
        #         print("unexpected arithmetic command")
        self.output.write("\n")
        return

    def write_push_pop(self, command, segment, index):
        match segment:
            case "constant":
                segment_symbol = str(index)
            case "local": 
                segment_symbol = "LCL"
            case "argument":
                segment_symbol = "ARG"
            case "this":
                segment_symbol = "THIS"
            case "that":
                segment_symbol = "THAT"
            case "pointer":
                if index == '0':
                    segment_symbol = "THIS"
                elif index == '1':
                    segment_symbol = "THAT"
            case "temp":
                segment_symbol = f"R{5 + index}"
            case "static":
                segment_symbol = f"{self.file_name}.{self.static_count}"
                self.static_count += 1
        match command:
            case "C_PUSH":
                self.output.write(f"@{segment_symbol}")
                # if segment_symbol in ["LCL, ARG, THIS, THAT"]:
                #     for i in range(index):
                #         self.output.write("A=A+1")
                # self.output.write(f"D=A")
                # self.output.write(f"@SP")
                # self.output.write(f"A=M")
                # self.output.write(f"M=D")
                # self.output.write(f"@SP")
                # self.output.write(f"M=M+1")
            case "C_POP":
                self.output.write(f"")
                # self.output.write(f"")
                # self.output.write(f"")
                # self.output.write(f"")
                # self.output.write(f"@${segment_symbol}")
                # self.output.write(f"M=D")
                # self.output.write(f"@SP")
                # self.output.write(f"M=M-1")
            case _:
                print("not a push/pop command")
        return

    def close(self):
        self.output.close()
        return