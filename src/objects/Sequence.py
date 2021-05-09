import copy


class Sequence:
    """Representation of a number sequence.
        Consists of a few useful functions connected with sequences."""

    def __init__(self, *args):
        """Sequence constructor.
            args - numbers of which the sequence will be composed of; if it's empty or not a list, the empty sequence will be created."""

        if len(args) == 0:
            self.data = []
        elif len(args) == 1 and isinstance(args[0], list):
            self.data = copy.deepcopy(args[0])
        else:
            print("Passed argument should be a list. Creating an empty sequence.")
            self.data = []

    def read_sequence_from_file(self, file_path):
        """Reads a sequence from file.
            file_path - path to file with sequence data"""

        with open(file_path, 'r') as f:
            self.data = []
            for line in f:
                line_data = [int(num) for num in line.split(' ')]
                self.data.extend(line_data)
        print("Sequence has been read from file.")

    def read_sequence_from_list(self, li):
        """Reads a sequence from a list.
            li - list of numbers of which the sequence will be composed of"""

        if isinstance(li, list):
            self.data = copy.deepcopy(li)
        else:
            print("Passed argument is not a list.")

    def __str__(self):
        """String representation of a sequence."""

        sequence_as_string = "(" + str(self.data[0])
        for i in range(1, len(self.data)):
            sequence_as_string = sequence_as_string + "," + str(self.data[i])
        sequence_as_string = sequence_as_string + ")"
        return sequence_as_string

    def __len__(self):
        """Returns length of a sequence."""

        return len(self.data)

    def __getitem__(self, index):
        """Returns certain item from a sequence.
            index - index of an item to get"""

        if index > len(self.data):
            print("Passed index is out of range.")
            return
        return self.data[index]
