class Parser:
    def __init__(self, input_path) -> None:
        with open(input_path, 'r') as input_file:
            self.input_lines = input_file.readlines()
        self.line_index = -1
        self.next_index = 0
        self.output_index = 0
        self.current_line = ""
        return

    def has_more_commands(self):
        self.next_index = self.line_index + 1
        while self.next_index < len(self.input_lines):
            next_line = self.input_lines[self.next_index].split("//")[0].strip('\n ')
            if next_line:
                return True
            self.next_index += 1
        return False

    def advance(self):
        self.line_index = self.next_index
        self.current_line = self.input_lines[self.line_index].split('//')[0].strip('\n ')
        return

    def command_type(self):
        if self.current_line.split()[0] in ["push", "pop"]:
            return f"C_{self.current_line.split()[0].upper()}"
        elif self.current_line.split()[0] in ["add", "sub", "neg", "eq", "gt", "lt", "and", "or", "not"]: 
            return "C_ARITHMETIC"

    def arg1(self):
        if self.command_type() in ["C_PUSH", "C_POP"]:
            return self.current_line.split()[1]
        elif self.command_type() == "C_ARITHMETIC":
            return self.current_line
    
    def arg2(self):
        return self.current_line.split()[2]
