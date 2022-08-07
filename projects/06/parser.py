class Parser:
    def __init__(self, input_file) -> None:
        self.cmd_list = input_file.read().splitlines()
        self.cmd_num = len(self.cmd_list)
        self.current_count = 0
        self.cmd_now = self.cmd_list[self.current_count]
    
    def has_more_commands(self):
        return self.current_count < self.cmd_num

    def advance(self):
        self.current_count += 1
        self.cmd_now = self.cmd_list[self.current_count]
        while(self.cmd_now == '' or self.cmd_now.isspace() or (self.cmd_now[0] == '/' and self.cmd_now[1] == '/')):
            self.current_count += 1
            if(self.current_count < self.cmd_num):
                self.cmd_now = self.cmd_list[self.current_count]
            else:
                break
        return

    def commandType(self):
        cmd_type_list = ['A_COMMAND', 'C_COMMAND', 'L_COMMAND']
        if(self.cmd_now[0] == '@'):
            return cmd_type_list[0]
        elif(self.cmd_now):
            return cmd_type_list[1]
        else:
            return cmd_type_list[0]

    def symbol(self):
        return

    def dest(self):
        return

    def comp(self):
        return

    def jump(self):
        return