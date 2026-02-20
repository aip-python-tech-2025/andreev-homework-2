
data = [
    'lorem ipsum dolor sit amet',
    'hello world',
    'goodbye world',
    'ga-ga-ga',
]

f = lambda s: s.count('a')
data.sort(key=f)
# data = sorted(data)
print(*data, sep='\n')
