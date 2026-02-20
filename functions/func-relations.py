
def s(a: int, b: int) -> int:
    return a + b


def reduce(operation, data: list, start):
    result = start
    for item in data:
        result = operation(result, item)
    return result


def get_operation(op: str):
    def add(a, b):
        return a + b
    def sub(a, b):
        return a - b
    def mul(a, b):
        return a * b
    def div(a, b):
        return a / b

    if op == '+':
        return add
    elif op == '-':
        return sub
    elif op == '*':
        return mul
    elif op == '/':
        return div
    else:
        raise Exception('Operation not supported')


print(reduce(s, [5, 6, 2, 0, 2], 0))
print(reduce(lambda a, b: a * b, [5, 6, 2, 2], 1))

operation = get_operation('*')
print(operation(4, 9))


print(s(1, 2))
get_sum = s
print(get_sum(1, 2))

del s
print(get_sum(1, 2))
