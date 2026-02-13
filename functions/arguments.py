
def s(a, b=0, *args, **kwargs):
    print(a, b, args, kwargs)
    return a + b + sum(args) + sum(kwargs.values())


print(s(7, 9))
print(s(b=9, a=7))
print(s(a=7, b=9))
print(s(7, b=9))
print(s(7))
print(s(7, 9, 15, 17))
print(s(7, 9, x=15, y=17))
