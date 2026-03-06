def multi_input():
    while True:
        s = input()
        if s == '':
            return 'End of input'
        yield s


for s in multi_input():
    print(s)
