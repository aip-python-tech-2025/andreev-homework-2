
from typing import Tuple, List, Dict, Union
from fractions import Fraction

Number = int | float | Fraction


def s(a: Number, b: Number) -> Number:
    return a + b


print(s(1, 2))
print(s(3.14, 1.72))
print(s(Fraction(0.5), Fraction(1, 3)))

data: List[int] = [1, 2, 3]
data.append('hello')
print(data)

words: dict[str, int] = {
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}

info: tuple[str, str, int, bool] = ('Nikolai', 'Andreev', 27, False)
