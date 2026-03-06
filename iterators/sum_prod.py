def sum_prod(a: int, b: int):
    for _ in range(10):
        yield a + b
        yield a * b


gen = sum_prod(3, 4)

print(gen)
print(gen.__iter__)
print(gen.__next__)

print(*sum_prod(1, 2))

for s in sum_prod(1, 2):
    print(s)
