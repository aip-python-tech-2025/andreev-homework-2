
def log(function):
    def wrapper(*args, **kwargs):
        print(f'Calling function \033[1;31m{function.__name__}()\033[0m')
        return function(*args, **kwargs)

    return wrapper


@log
def add(a: int, b: int) -> int:
    return a + b


@log
def sub(a: int, b: int) -> int:
    return a - b


@log
def hi():
    return 'hi'


# hi = log(hi)
print(hi())
print(hi())

print(add(7, 3))
print(sub(7, 3))
