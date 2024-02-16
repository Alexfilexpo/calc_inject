class Operation:
    def execute(self, operand1, operand2):
        raise NotImplementedError()


class Addition(Operation):
    def execute(self, operand1, operand2):
        return operand1 + operand2


class Subtraction(Operation):
    def execute(self, operand1, operand2):
        return operand1 - operand2


class Multiplication(Operation):
    def execute(self, operand1, operand2):
        return operand1 * operand2


class Division(Operation):
    def execute(self, operand1, operand2):
        if operand1 == 0 or operand2 == 0:
            return "Cannot divide by zero"
        return operand1 / operand2
