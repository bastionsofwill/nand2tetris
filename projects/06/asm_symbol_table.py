class SymbolTable:
    def __init__(self) -> None:
        self.symbol_table = {}
        self.symbol_table["SP"] = 0
        self.symbol_table["LCL"] = 1
        self.symbol_table["ARG"] = 2
        self.symbol_table["THIS"] = 3
        self.symbol_table["THAT"] = 4
        self.symbol_table["SCREEN"] = 16384
        self.symbol_table["KBD"] = 24576
        for i in range(16):
            self.symbol_table[f"R{i}"] = i
        self.var_index = 16

    def add_entry(self, symbol, address = None):
        if address:
            self.symbol_table[symbol] = address
        else:
            self.symbol_table[symbol] = self.var_index
            self.var_index += 1
        return None

    def contains(self, symbol):
        return symbol in self.symbol_table

    def get_address(self, symbol):
        return bin(int(self.symbol_table[symbol]))[2:]