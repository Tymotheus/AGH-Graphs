class Sequence:
    def __init__(self):
        self.data = []

    def read_sequence_from_file(self, file_path):
        with open(file_path, 'r') as f:
            self.data = []
            for line in f:
                line_data = [int(num) for num in line.split(' ')]
                self.data.extend(line_data)
        print("Sequence has been read from file.")

    def read_sequence_from_list(self, li):
        if isinstance(li, list):
            self.data = li.copy()
        else:
            print("Passed argument is not a list.")

    def __str__(self):
        res = "(" + str(self.data[0])
        for i in range(1, len(self.data)):
            res = res + "," + str(self.data[i])
        res = res + ")"
        return res
