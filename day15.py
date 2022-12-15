manhattan = lambda v1, v2: abs(v2[0]-v1[0]) + abs(v2[1]-v1[1])
dist_to_2MM = lambda v: abs(v[1]-2000000)

v = ['',] * 10
x_reject_segs = []
with open('input15', 'r') as file:
    for line in file:
        for n, word in enumerate(line.split()):
            v[n] = ''.join(n for n in word if n in '-0123456789')
        sx, sy, bx, by = map(int, (v[2], v[3], v[8], v[9]))
        s, b = (sx, sy), (bx, by)
        spread = manhattan(s, b)
        offset = dist_to_2MM(s)
        if offset > spread:
            continue  # Not in range
        rem = spread - offset  # Remaining x span
        x_reject_segs.append([s[0] - rem, s[0] + rem])

x_reject_segs.sort()
x_reject = [x_reject_segs[0]]

for seg in x_reject_segs:
    xr_tail = x_reject[-1]
    if seg[0] <= xr_tail[1]:
        xr_tail[1] = max(xr_tail[1], seg[1])
    else:
        x_reject.append(seg)

rejected = sum([e - s for s, e in x_reject])

print(f'Part A: {rejected}')
print(f'Part B: {0}')
