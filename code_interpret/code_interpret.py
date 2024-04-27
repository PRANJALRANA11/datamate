
class Interpreter:
    def __init__(self):
        self.code = ""
        self.data = [0] * 30000
        self.pointer = 0
        self.code_pointer = 0