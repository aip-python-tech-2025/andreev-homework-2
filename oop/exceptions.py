def get_sum(a, b):
    if a.isdecimal() and b.isdecimal():
        s = int(a) + int(b)
        return True

    return False


def get_div(a, b):
    if not (a.isdecimal() and b.isdecimal()):
        return 1, None
    elif int(b) == 0:
        return 2, None
    else:
        s = int(a) // int(b)
        return 0, s


def divide(a, b):
    return a // b


def get_data(x):
    try:
        return 100 // x
    except ZeroDivisionError:
        return None
    finally:
        print('Closing connection...')
        # return []


try:
    a = int(input())
    b = int(input())
    print(divide(a, b))
except ZeroDivisionError:
    print('Division by zero')
except ValueError:
    print('Wrong input')
finally:
    print('This will be executed')

# print([] + 1)

print(get_data(5))
print(get_data(0))
