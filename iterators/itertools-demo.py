from itertools import combinations, batched


def count():
    x = 1
    while True:
        yield x
        x = x + 1


stream = filter(lambda el: el % 100 == 0, map(lambda el: el ** 2, count()))
another_stream = (el ** 2 for el in count() if el ** 2 % 100 == 0)
third_stream = ()

for x in zip(batched(another_stream, 2), range(10)):
    print(x)

# for x in another_stream:
#     print(x)
