import random
from math import isqrt, sqrt


def factorial(x):
    res = 1
    for i in range(1, x + 1):
        res *= i
    return res


n, k = 9, 5

# C_n^k = n! // k! // (n-k)!

f_n = factorial(n)
f_k = factorial(k)
f_nk = factorial(n - k)

print(f_n // f_k // f_nk)

x = random.randint(0, 10000)
print(x, isqrt(x), sqrt(x))
