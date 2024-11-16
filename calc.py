class Stack:
    def __init__(self):
        # Initialize an empty list to store stack items
        self.items = []

    def is_empty(self):
        # Return True if the stack is empty, otherwise False
        return len(self.items) == 0

    def push(self, item):
        # Add an item to the top of the stack
        self.items.append(item)

    def pop(self):
        # Remove and return the top item from the stack if it's not empty
        # If the stack is empty, return None
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        # Return the top item without removing it if the stack is not empty
        # If the stack is empty, return None
        if not self.is_empty():
            return self.items[-1]
        return None


def apply_operator(num_stack, op_stack):
    # Pop the top operator from op_stack
    operator = op_stack.pop()
    # Pop the top two numbers from num_stack
    b = num_stack.pop()
    a = num_stack.pop()
    
    # Perform the operation based on the operator
    if operator == '+':
        num_stack.push(a + b)
    elif operator == '-':
        num_stack.push(a - b)
    elif operator == '*':
        num_stack.push(a * b)
    elif operator == '/':
        num_stack.push(a / b)


def precedence(op):
    # Define precedence for operators
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    return 0


def evaluate_expression(expression):
    # Initialize two stacks: one for numbers and one for operators
    num_stack = Stack()  # Stack for numbers
    op_stack = Stack()  # Stack for operators
    
    i = 0
    while i < len(expression):
        char = expression[i]
        
        # Ignore whitespace characters
        if char == ' ':
            i += 1
            continue
        
        # If the character is a digit, parse the number
        if char.isdigit():
            num = 0
            while i < len(expression) and expression[i].isdigit():
                num = num * 10 + int(expression[i])
                i += 1
            num_stack.push(num)
            continue
        
        # If the character is an opening parenthesis '(', push it to op_stack
        elif char == '(':
            op_stack.push(char)
        
        # If the character is a closing parenthesis ')', pop and apply operators until '(' is found
        elif char == ')':
            while op_stack.peek() != '(':
                apply_operator(num_stack, op_stack)
            op_stack.pop()  # Pop the '('
        
        # If the character is an operator (+, -, *, /)
        elif char in "+-*/":
            while (not op_stack.is_empty() and
                   precedence(op_stack.peek()) >= precedence(char)):
                apply_operator(num_stack, op_stack)
            op_stack.push(char)
        
        # Move to the next character
        i += 1
    
    # After the loop, apply any remaining operators in op_stack
    while not op_stack.is_empty():
        apply_operator(num_stack, op_stack)
    
    # Return the final result from num_stack
    return num_stack.pop()


# Test cases
expression1 = "(((6+9)/3)*(6-4))"
expression2 = "10 + (2 * (6 + 4))"
expression3 = "100 * (2 + 12) / 4"
# Expected output: 10, 30, 350 respectively
print(evaluate_expression(expression1))  # 10
print(evaluate_expression(expression2))  # 30
print(evaluate_expression(expression3))  # 350

