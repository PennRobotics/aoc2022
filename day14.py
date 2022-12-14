DEBUG = print if False else lambda *s: None

#from * import _

CONST = None

def fn():
    global x
    DEBUG(''.join([' ']*x) + f'')
    pass

#with open('sample14', 'r') as file:
with open('input14', 'r') as file:
    coords = file.read().rstrip('\n').replace('\n',' -> ').split(' -> ')
x = []; y = []
for coord in coords:
    xs, ys = coord.split(',')
    x.append(int(xs))
    y.append(int(ys))
print((min(x), max(x)))
print((min(y), max(y)))

print(f'Part A: {0}')
print(f'Part B: {0}')
