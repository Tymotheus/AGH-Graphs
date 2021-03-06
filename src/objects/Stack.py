import copy


class Stack:
    def __init__(self, *args):
        if len(args) == 0:
            self.data = []
        elif len(args) == 1 and isinstance(args[0], list):
            self.data = copy.deepcopy(args[0])
        else:
            print("Passed argument should be a list. Creating an empty stack.")
            self.data = []

    def read_stack_from_file(self, file_path):
        with open(file_path, 'r') as f:
            self.data = []
            for line in f:
                line_data = [int(num) for num in line.split(' ')]
                self.data.extend(line_data)
        print("Stack has been read from file.")

    def read_stack_from_list(self, li):
        if isinstance(li, list):
            self.data = copy.deepcopy(li)
        else:
            print("Passed argument is not a list.")

    def is_empty(self):
        if len(self) == 0:
            return True
        return False

    def push(self, value_to_add):
        if len(self) == 0 or isinstance(value_to_add, type(self.data[0])):
            self.data.append(value_to_add)
        else:
            print("Passed argument does not match the type of objects in stack.")

    def pop(self):
        return self.data.pop()

    def unpack_to_list(self):
        stack_as_list = []
        while len(self) > 0:
            stack_as_list.append(self.pop())
        return stack_as_list

    def peek(self):
        return self.data[len(self)-1]

    def __str__(self):
        stack_as_string = "[]"
        if len(self) > 0:
            stack_as_string = "[" + str(self.data[0])
            for i in range(1, len(self.data)):
                stack_as_string = stack_as_string + "," + str(self.data[i])
            stack_as_string = stack_as_string + "]"
        return stack_as_string

    def __len__(self):
        return len(self.data)
