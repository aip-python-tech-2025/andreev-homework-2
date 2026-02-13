
# Неизменяемые
x = 10
s = 'hello world'
# Изменяемые
data = [1, 5, 4]

print(type(x))
print(type(int))
print(type(str))
print(type(type))

another = data
another.append(0)
print(data)
print(another)

print(id(data))
print(id(another))

y = x
print(id(x))
print(id(y))
y += 134567654
print(x, y)
print(id(x))
print(id(y))
