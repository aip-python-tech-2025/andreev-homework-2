class Counter:
    x: int
    start: int

    def __init__(self, x: int):
        self.x = x - 1
        self.start = self.x

    def __iter__(self):
        self.x = self.start
        return self

    def __next__(self):
        self.x += 1
        return self.x


counter = Counter(9)

for x in counter:
    print(x)
    if x == 20:
        break

for x in counter:
    print(x)
    if x == 30:
        break
