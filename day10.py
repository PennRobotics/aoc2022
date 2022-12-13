X = 1; cyc = 0
sigs = []

targets = iter(range(20,261,40))
target = next(targets)

print(f'Part B:')

with open('input10', 'r') as file:
#with open('sample10', 'r') as file:
    for line in file:
        if line[0] == 'n':
            dcyc = 1
            dx = 0
        else:
            dcyc = 2
            dx = int(line.split(' ')[1])
        while dcyc != 0:
            cyc += 1
            dcyc -= 1
            if abs(((cyc - 1) % 40) - X) < 2:
                print('#', end='')
            else:
                print(' ', end='')
            if cyc % 40 == 0:
                print('')
            if cyc == target:
                sigs.append(target * X)
                try:
                    target = next(targets)
                except StopIteration:
                    pass
            if dcyc == 0:
                X += dx

print(f'Part A: {sum(sigs)}')
