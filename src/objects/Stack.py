import copy


class Stack:
    """Representation of a number stack.
        Consists of a few useful functions connected with stack."""

    def __init__(self, *args):
        """Stack constructor.
             args - numbers of which the stack will be composed of; if it's empty or not a list, the empty stack will be created."""

        if len(args) == 0:
            self.data = []
        elif len(args) == 1 and isinstance(args[0], list):
            self.data = copy.deepcopy(args[0])
        else:
            print("Passed argument should be a list. Creating an empty stack.")
            self.data = []

    def read_stack_from_file(self, file_path):
        """Reading a stack from file.
            file_path - path to file with stack data"""

        with open(file_path, 'r') as f:
            self.data = []
            for line in f:
                line_data = [int(num) for num in line.split(' ')]
                self.data.extend(line_data)
        print("Stack has been read from file.")

    def read_stack_from_list(self, li):
        """Reading a stack from a list.
            li - list of numbers of which the stack will be composed of"""

        if isinstance(li, list):
            self.data = copy.deepcopy(li)
        else:
            print("Passed argument is not a list.")

    def is_empty(self):
        """Returns True whether the stack is empty and False otherwise."""

        if len(self) == 0:
            return True
        return False

    def push(self, value_to_add):
        """Adds an element to the stack.
            value_to_add - value to be pushed on stack."""

        if len(self) == 0 or isinstance(value_to_add, type(self.data[0])):
            self.data.append(value_to_add)
        else:
            print("Passed argument does not match the type of objects in stack.")

    def pop(self):
        """Removes the top element from stack and returns it's value."""

        return self.data.pop()

    def unpack_to_list(self):
        """Unpacks stack to list."""

        stack_as_list = []
        while len(self) > 0:
            stack_as_list.append(self.pop())
        return stack_as_list

    def peek(self):
        """Returns the value of the top element of stack (does not remove it)."""

        return self.data[len(self)-1]

    def __str__(self):
        """String representation of a stack."""

        stack_as_string = "[]"
        if len(self) > 0:
            stack_as_string = "[" + str(self.data[0])
            for i in range(1, len(self.data)):
                stack_as_string = stack_as_string + "," + str(self.data[i])
            stack_as_string = stack_as_string + "]"
        return stack_as_string

    def __len__(self):
        """Returns length of a stack."""

        return len(self.data)
