class MultiInput:
    def __iter__(self):
        return self

    def __next__(self):
        s = input()
        if s == '':
            raise StopIteration('End of input')
        return s


multi_input = MultiInput()
for s in multi_input:
    print('New line:', s)
