
import inspect
import traceback

def greet(name='Anonymous'):
    print(len(inspect.stack()))
    return f"Hello {name}"


greeting_1 = greet('John')
greeting_default = greet()

print(greeting_1, greeting_default)
