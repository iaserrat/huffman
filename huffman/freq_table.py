from collections import Counter, OrderedDict


class FreqTable(object):
    def __init__(self):
        self.table = {}
        self.data = None

    def get_data(self, lines):
        self.data = ''.join(lines).replace('\n', '')
        return self.data

    def get_table_for_file(self, file_name):
        with open(file_name, 'r') as f:
            data = self.get_data(f.readlines())
            self.table = OrderedDict(sorted(Counter(data).items()))
            return self.table
