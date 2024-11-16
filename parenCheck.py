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


def is_balanced(expression):
    # Create a stack to keep track of opening parentheses
    stack = Stack()
    # Define matching pairs for parentheses
    opening = "({["
    closing = ")}]"
    matches = {')': '(', '}': '{', ']': '['}
    
    # Loop through each character in the expression
    for char in expression:
        # Check if the character is an opening parenthesis
        if char in opening:
            # Push the opening parenthesis to the stack
            stack.push(char)
        
        # Check if the character is a closing parenthesis
        elif char in closing:
            # If stack is empty or top of stack doesn't match the closing parenthesis, return False
            top = stack.pop()  # Pop the top item from the stack
            if top != matches[char]:
                return False
    
    # If stack is empty, all parentheses were matched; otherwise, return False
    return stack.is_empty()


# Test cases
expression1 = "({X+Y}*Z)"       # Expected output: True
expression2 = "{X+Y}*Z)"        # Expected output: False
expression3 = "({X+Y}*Z"        # Expected output: False
expression4 = "[A+B]*({X+Y}]*Z)"# Expected output: False

print(is_balanced(expression1))  # True
print(is_balanced(expression2))  # False
print(is_balanced(expression3))  # False
print(is_balanced(expression4))  # False

