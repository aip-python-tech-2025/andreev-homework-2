import time
from concurrent.futures import ThreadPoolExecutor

def cpu_task(n):
    s = 0
    for i in range(n):
        s += i*i
    return s

N = 20_000_000
t0 = time.perf_counter()
for i in range(4):
    cpu_task(N)
print("последовательно:", round(time.perf_counter() - t0, 3), "сек")

t0 = time.perf_counter()
with ThreadPoolExecutor(max_workers=4) as ex:
    list(ex.map(cpu_task, [N, N, N, N]))
print("4 потока:", round(time.perf_counter() - t0, 3), "сек")
