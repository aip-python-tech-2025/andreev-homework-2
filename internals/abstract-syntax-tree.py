
import ast

code = '''
flag = False
if flag:
    a = 1 + 2 * 5
else:
    a = 0
print(b)'''

tree = ast.parse(code)
print(ast.dump(tree, indent=2))
