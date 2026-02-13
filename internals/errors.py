code = """x = 10 +
print(x)"""
obj = compile(code, '<string>', 'exec')
exec(obj)
