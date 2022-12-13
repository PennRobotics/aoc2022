import math

trees_2d = []
with open('input08', 'r') as file:
    for line in file:
        trees_2d.append([int(e) for e in line.rstrip('\n')])
sz = len(trees_2d)
trees = [x for y in trees_2d for x in y]
visible = [0] * (sz**2)

start_idx_ltr = lambda i: i
start_idx_topdown = lambda i: sz * i
start_idx_rtl = lambda i: sz**2 - i - 1
start_idx_bottomup = lambda i: sz**2 - sz * i - 1

next_from_left = lambda i: i + 1 if i % sz != sz - 1 else -1
next_from_right = lambda i: i - 1 if i % sz != 0 else -1
next_from_top = lambda i: i + sz if i // sz != sz - 1 else -1
next_from_bottom = lambda i: i - sz if i // sz != 0 else -1

def check_tree_line(idx, next_fn):
    h = -1
    while h != 9 and idx != -1:
        if trees[idx] > h:
            h = trees[idx]
            if visible[idx] == 0:
                visible[idx] = 1
        idx = next_fn(idx)
    pass

for x in range(sz):
    check_tree_line(start_idx_ltr(x), next_from_top)         # Check left-to-right from top
    check_tree_line(start_idx_topdown(x), next_from_left)    # Check top-to-bottom from left
    check_tree_line(start_idx_rtl(x), next_from_bottom)      # Check right-to-left from bottom
    check_tree_line(start_idx_bottomup(x), next_from_right)  # Check bottom-to-top from right

def get_viewing_distance(idx, next_fn):
    h = trees[idx]
    d = 1
    idx = next_fn(idx)
    while h > trees[idx]:
        idx = next_fn(idx)
        if idx == -1:
            break
        d += 1
    return d

max_vd = 0
factors = [0, 0, 0, 0]
for x in range(sz*sz):
    if x < sz or x % sz == 0 or x % sz == sz - 1 or x > sz**2 - sz - 1:
        continue
    factors[0] = get_viewing_distance(x, next_from_bottom)  # Look up
    factors[1] = get_viewing_distance(x, next_from_top)     # Look down
    factors[2] = get_viewing_distance(x, next_from_right)   # Look all around
    factors[3] = get_viewing_distance(x, next_from_left)    # ...
    vd = math.prod(factors)
    max_vd = vd if vd > max_vd else max_vd

print(f'Part A: {sum(visible)}')
print(f'Part B: {max_vd}')
