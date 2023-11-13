



class RegisterMachine:
    def __init__(self, commands, size=100):
        self.commands = commands
        self.registers = [0]*size
        self.current_command = 0
        self.command_dict = {
            'load': self.load,
            'cload': self.cload,
            'store': self.store,
            'add': self.add,
            'cadd': self.cadd,
            'sub': self.sub,
            'csub': self.csub,
            'mul': self.mul,
            'cmul': self.cmul,
            'div': self.div,
            'cdiv': self.cdiv,
            'goto': self.goto,
            'ifgoto': self.ifgoto,
            'end': self.end
        }

    def run(self):
        while self.current_command < len(self.commands):
            self.execute_command(self.current_command)
            self.current_command += 1


    def execute_command(self, line):
        command = self.commands[line].split(" ")
        self.command_dict[command[0].lower()](int(command[1]))

    def load(self, reg):
        self.registers[0] = self.registers[reg]

    def cload(self, const):
        self.registers[0] = const

    def store(self, reg):
        self.registers[reg] = self.registers[0]

    def add(self, reg):
        self.registers[0] += self.registers[reg]

    def cadd(self, const):
        self.registers[0] += const

    def sub(self, reg):
        self.registers[0] -= self.registers[reg]

    def csub(self, const):
        self.registers[0] -= const

    def mul(self, reg):
        self.registers[0] *= self.registers[reg]

    def cmul(self, const):
        self.registers[0] *= const

    def div(self, reg):
        self.registers[0] //= self.registers[reg]

    def cdiv(self, const):
        self.registers[0] //= const

    def goto(self, line):
        self.current_command = line - 2

    def ifgoto(self, command):
        if self.registers[0] == 0:
            self.goto(command)

    def end(self, c):
        self.current_command = len(self.commands)