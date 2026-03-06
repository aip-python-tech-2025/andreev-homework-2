data = [1, 2, 3]

iterator = iter(data)

while True:
    try:
        x = next(iterator)
    except StopIteration:
        break
    print(x)

# for x in data:
#     print(x)
