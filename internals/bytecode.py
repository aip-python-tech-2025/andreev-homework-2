
import dis

code = '''a = 1 + 2 * 5
print(a)'''
obj = compile(code, '<string>', 'exec')
print(obj.co_consts)
print(obj.co_names)
dis.dis(obj)
