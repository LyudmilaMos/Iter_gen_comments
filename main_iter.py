nested_list = [['a', 'b', 'c'],	['d', 'e', 'f', 'h', False], [1, 2, None]]


class FlatIterator:

    def __init__(self, n_list):
        self.n_list = n_list
        self.cursor = -1
        self.l_list = len(self.n_list)

    def __iter__(self):
        self.cursor += 1
        self.n_cursor = 0
        return self

    def __next__(self):
        if self.n_cursor == len(self.n_list[self.cursor]):
            iter(self)
        if self.cursor == self.l_list:
            raise StopIteration
        self.n_cursor += 1
        return self.n_list[self.cursor][self.n_cursor - 1]


if __name__ == '__main__':
    flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)
