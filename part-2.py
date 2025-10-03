greeting = '''Hello World!
This is multiline string'''

print(greeting)
print(greeting[4])
print(greeting[-2])

ind = 8
print(greeting[ind])

for char in greeting:
    print(ord(char))

print(greeting[2:9], end='\n\n')
print(greeting[:9], end='\n\n')
print(greeting[9:], end='\n\n')
print(greeting[:], end='\n\n')
print(greeting[2:9:2], end='\n\n')
print(greeting[9:2:-1], end='\n\n')
print(greeting[::-1], end='\n\n')

print(len(greeting))

print(greeting.count('ll'))
print(greeting.index('l'))
print(greeting.rindex('l'))

print(greeting.capitalize())
print(greeting.title())
print(greeting.upper())
print(greeting.lower())
print(greeting.swapcase())

print(greeting.split())

# greeting[0] = 'h'
# print(greeting)

data = [5, 8, 7, 2, 4, 6, 9]
print(data)

data[-1] = 0
print(data)

print(data[3])
print(len(data))

print(data[2:6])
print(data[6:2:-1])

print(data.index(2))
print(min(data), max(data), sum(data))

data.append(10)
print(data)

data.pop(1)
print(data)

data.sort()
print(data)

data.reverse()
print(data)

print(data + [8, 7, 3])
print(data * 2)

print(list(range(10)))

another_data = (1, 7, 9)
print(another_data)

print(tuple(range(10)))

phones = {'242-00-00': 'Общий отдел Университета ИТМО', '555-35-35': 'Мошенники'}
print(phones)
print(phones['242-00-00'])
print(phones['555-35-35'])

phones['123-45-67'] = 'Служба такси'
print(phones)

phones.pop('123-45-67')
print(phones)

phones['555-35-35'] = 'Кредитное бюро'

print(len(phones))

for key in phones:
    print(key, phones[key])
