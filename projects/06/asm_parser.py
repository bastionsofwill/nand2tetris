class Parser:
    def __init__(self, input_path) -> None:
        with open(input_path, 'r') as input_file:
            self.input_lines = input_file.readlines()
        self.line_index = -1
        self.next_index = 0
        self.output_index = 0
        self.current_line = ""

    def has_more_lines(self):
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
        return None
    
    def instruction_type(self):
        if self.current_line[0] == '@': # A-command
            return "A_INSTRUCTION"
        elif self.current_line[0] == '(':
            return "L_INSTRUCTION"
        else:
            return "C_INSTRUCTION"
        
    def symbol(self):
        match self.instruction_type():
            case "A_INSTRUCTION":
                return self.current_line[1:]
            case "L_INSTRUCTION":
                return self.current_line[1:-1]

    def dest(self):
        if '=' in self.current_line:
            if ';' in self.current_line:
                return self.current_line.split(';')[0].split("=")[0]
            else:
                return self.current_line.split('=')[0]
        return ""

    def comp(self):
        if ';' in self.current_line:
            if '=' in self.current_line:
                return self.current_line.split(';')[0].split("=")[1]
            else: 
                return self.current_line.split(';')[0]
        elif '=' in self.current_line:
            return self.current_line.split('=')[1]
        return self.current_line

    def jump(self):
        if ';' in self.current_line:
            return self.current_line.split(";")[1]
        return ""