import os

class Parser:
    def __init__(self, input_path) -> None:
        self.input_path = os.path.split(os.path.abspath(input_path))
        self.output_path = input_path[0]
        self.output_name = input_path[1].split('.')[0]
        self.input_file = open(self.input_path, 'r')
        self.output_file = open(f'{self.output_path}/{self.output_name}.hack', 'w')
        pass
    def has_more_commands():
        return False
    def advance():
        return None
    def command_type():
        return "A_COMMAND"
    def symbol():
        return ""
    def dest():
        return ""
    def comp():
        return ""
    def jump():
        return ""