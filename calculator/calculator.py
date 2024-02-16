from calculator.basic_operations import Addition, Subtraction, Multiplication, Division


class Calculator:
    def __init__(self):
        # Basic operations will be included
        self.operations = {
            "+": Addition(),
            "-": Subtraction(),
            "*": Multiplication(),
            "/": Division()
        }

    def add_operation(self, symbol, operation):
        """Adds or replaces an operation in the calculator."""
        self.operations[symbol] = operation

    def perform_operation(self, operator, operand1, operand2):
        """Performs the given operation if available."""
        operation = self.operations.get(operator)
        return operation.execute(operand1, operand2)
