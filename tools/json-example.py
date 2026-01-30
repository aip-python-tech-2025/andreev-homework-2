import json

file = open('data.json', encoding='utf-8')
data = json.load(file)
file.close()

print(data['data']['description'])

data['data']['description'] = 'Очень подробный и точный перевод'
file = open('updated.json', 'w', encoding='utf-8')
json.dump(data, file, ensure_ascii=False, indent=2)
file.close()
