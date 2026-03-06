from typing import Any


class Repeater:
    x: Any

    def __init__(self, x: Any):
        self.x = x

    def __iter__(self):
        return self

    def __next__(self):
        return self.x


repeater = Repeater(12)
for x in repeater:
    print(x)
