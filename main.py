from register import RegisterMachine

def load_commands(filename):
    with open(filename, 'r') as f:
        return f.readlines()

def load_inputs(filename):
    with open(filename, 'r') as f:
        return [int(x) for x in f.readlines()]

def main():
    inputs = load_inputs('inputs.txt')
    register = RegisterMachine(load_commands('commands.rm'), len(inputs))
    register.registers = inputs
    register.run()
    print(register.registers)


if __name__ == '__main__':
    main()