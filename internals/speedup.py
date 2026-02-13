
import time

t0 = time.perf_counter()
s = sum(range(25600000))
t1 = time.perf_counter()
print(s, t1 - t0)

s = 0
t0 = time.perf_counter()
for i in range(25600000):
    s += i
t1 = time.perf_counter()
print(s, t1 - t0)

l = list(range(10000000))
s = set(range(10000000))

t0 = time.perf_counter()
print(4999999 in l)
t1 = time.perf_counter()
print(t1 - t0)

t0 = time.perf_counter()
print(4999999 in s)
t1 = time.perf_counter()
print(t1 - t0)
