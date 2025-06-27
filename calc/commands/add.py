from calc.command import Command

class AddCommand(Command):
    def execute(self, a, b):
        return float(a) + float(b)
