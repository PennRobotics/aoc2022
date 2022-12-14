DEBUG = print if False else lambda *s: None

#from * import _

CONST = None

def fn():
    global x
    DEBUG(''.join([' ']*x) + f'')
    pass

with open('input14', 'r') as file:
    contents = file.read().rstrip('\n')

print(f'Part A: {0}')
print(f'Part B: {0}')
