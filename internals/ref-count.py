
import sys

data = [1, 2, 3]
another = data
print(sys.getrefcount(data))

del data
print(another)
print(sys.getrefcount(another))

del another

x = 256
print(sys.getrefcount(x))
