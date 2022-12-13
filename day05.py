crates = ['']

with open('input05', 'r') as file:
    contents = file.read().rstrip('\n')

unparsed_state, instructions = contents.split('\n\n')

# Parse input into array of variable-length strings, `crates`
state_lines = unparsed_state.split('\n')
max_line_len = max([len(l) for l in state_lines])
for i in range(len(state_lines)):
    state_lines[i] = state_lines[i].ljust(max_line_len)
reject_idx = -1
for column in zip(*state_lines[:-1]):
    if not reject_idx:
        crates.append(''.join(column)[::-1].strip())
    reject_idx = reject_idx + 1 if reject_idx < 3 else 0

import copy
b_crates = copy.deepcopy(crates)

for inst in instructions.split('\n'):
    mask = lambda a: (a[1], a[3], a[5])
    cnt, src, dest = map(int, mask(inst.split(' ')))

    crates[src], temp = crates[src][:-cnt], crates[src][-cnt:]
    crates[dest] += temp[::-1]

    b_crates[src], temp = b_crates[src][:-cnt], b_crates[src][-cnt:]
    b_crates[dest] += temp

top = lambda i, crate_array: crate_array[i][-1]
tops = lambda crate_array: ''.join([top(c, crate_array) for c in range(1, len(crate_array))])

print(f'Part A: {tops(crates)}')
print(f'Part B: {tops(b_crates)}')
