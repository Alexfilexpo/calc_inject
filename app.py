from flask import Flask, request, render_template
from calculator.calculator import Calculator
from calculator.basic_operations import Operation

app = Flask(__name__)
calculator = Calculator()


# Example of dependency injection. Let's define a new operation for exponentiation
# class Exponentiation(Operation):
#     """Define exponentiation operation that raises operand1 to the power of operand2."""
#
#     def execute(self, operand1, operand2):
#         return operand1 ** operand2
#
#
# # Adding exponentiation operation to the calculator
# calculator.add_operation("**", Exponentiation())


def determine_color(result):
    try:
        num_result = float(result)
        color = "green" if num_result % 2 == 0 else "red"
    except ValueError:
        color = "black"  # Default color if result is not a number or an error message
    return color


@app.route('/', methods=['GET', 'POST'])
def index():
    """Handle GET and POST requests for the calculator operation."""
    if request.method == 'POST':
        operand1_text = request.form.get('operand1', '0')
        operand2_text = request.form.get('operand2', '0')

        try:
            operand1 = float(operand1_text) if '.' in operand1_text else int(operand1_text)
            operand2 = float(operand2_text) if '.' in operand2_text else int(operand2_text)
        except ValueError:
            return render_template('index.html', operators=list(calculator.operations.keys()),
                                   operand1=operand1_text, operand2=operand2_text, result="Invalid operand type")

        operator = request.form.get('operator', '+')  # Default to addition if not specified

        result = calculator.perform_operation(operator, operand1, operand2)

        color = determine_color(result)

        if isinstance(result, float):
            result = f"{result:.4f}"

        return render_template('index.html', operators=list(calculator.operations.keys()),
                               operand1=operand1, operand2=operand2, result=result, color=color)
    else:
        return render_template('index.html', operators=list(calculator.operations.keys()),
                               operand1=None, operand2=None, result=None, color="black")


if __name__ == '__main__':
    app.run(debug=True)
