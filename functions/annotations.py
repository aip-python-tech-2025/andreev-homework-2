
import requests


class Point:
    x: int
    y: int

    def __init__(self):
        self.x = 5
        self.y = 7


def s(a: int, b: int) -> int:
    return a + b


x: int = 5
print(x)

x = 'hello'
print(x)

greet: str = 'Hello World'
print(greet)

res: requests.Response = requests.get('https://httpbin.org/get')
res.raise_for_status()
print(res.text)

print(s('98', 5))
