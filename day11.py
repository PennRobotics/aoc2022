from math import prod

get_trailing_num = lambda s: int(s[::-1].split(' ')[0][::-1])

monkey = []

with open('input11', 'r') as file:
#with open('sample11', 'r') as file:
    while True:
        #idx = int(file.readline().replace(':', ' ').split(' ')[1])
        file.readline()
        items = list(map(int, file.readline().split(':')[1].split(',')))
        eval_fn = file.readline().split('= ')[1].rstrip('\n')
        div_check = get_trailing_num(file.readline())
        true_dest = get_trailing_num(file.readline())
        false_dest = get_trailing_num(file.readline())
        monkey.append([items, eval_fn, div_check, true_dest, false_dest, 0])
        if file.readline() == '':
            break


# Part A
### NUM_ROUNDS = 20
### for _ in range(NUM_ROUNDS):
###     for i, [its, fn, dv, dt, df, n] in enumerate(monkey):
###         for old in its:
###             n += 1
###             new = eval(fn) // 3
###             dest = df if new % dv else dt
###             monkey[dest][0].append(new)
###         monkey[i][0] = []
###         monkey[i][5] = n
### 
### inspection_count_list = sorted([e[5] for e in monkey])
### 
### a = inspection_count_list[-2] * inspection_count_list[-1]
### 
### print(f'Part A: {a}')

# Part B
common_modulo = prod([e[2] for e in monkey])

NUM_ROUNDS = 10000
for _ in range(NUM_ROUNDS):
    for i, [its, fn, dv, dt, df, n] in enumerate(monkey):
        for old in its:
            n += 1
            new = eval(fn) % common_modulo
            dest = df if new % dv else dt
            monkey[dest][0].append(new)
        monkey[i][0] = []
        monkey[i][5] = n

inspection_count_list = sorted([e[5] for e in monkey])

b = inspection_count_list[-2] * inspection_count_list[-1]

print(f'Part B: {b}')
