print('Hello World!', 5, False, sep='\n', end='\nThis is the end of print call\n')

num = int(input())
print(num * 2)

if num % 2 == 0:
    print('Число чётное')
elif num % 3 == 0:
    print('Число делится на 3')
else:
    print('Число не делится ни на 2, ни на 3')

while num ** 2 < 1000:
    print(num, num ** 2)
    num += 1
    if num % 5 == 0:
        continue
    print('Test')
else:
    print('Completed')

# and, or, not

if num < 50 or num ** 2 > 2000:
    print(num)

for x in 1, 2, 3, 4:
    print(x)

for i in range(10):
    print(i)

for i in range(11, 16):
    print(i)

for i in range(30, 26, -1):
    print(i+1)

print('Hello Git!')

print('Git & PyCharm Branch Test')
x = float(input())
print(x ** 2)
