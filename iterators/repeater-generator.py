from typing import Any


def repeater(x: Any):
    while True:
        yield x


for x in repeater(5):
    print(x)
