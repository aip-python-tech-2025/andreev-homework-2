import time
from concurrent.futures import ThreadPoolExecutor

def io_task():
    time.sleep(0.2)
    return 1

t0 = time.perf_counter()
for _ in range(20):
    io_task()
print("последовательно:", round(time.perf_counter() - t0, 3), "сек")

t0 = time.perf_counter()
with ThreadPoolExecutor(max_workers=10) as ex:
    list(ex.map(lambda _: io_task(), range(20)))
print("потоки:", round(time.perf_counter() - t0, 3), "сек")