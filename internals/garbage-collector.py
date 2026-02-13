
import gc
from sys import getrefcount

print(gc.collect())

a = [1, 2, 3]
a.append(a)
print(a)

x = [4, 5, 6]
y = [7, 8, 9]
x.append(y)
y.append(x)

print(getrefcount(a))
del x
del y
del a

print(gc.collect())
