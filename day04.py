contains = 0; overlaps = 0

with open('input04', 'r') as file:
    for line in file:
        s1, e1, s2, e2 = map(int, line.strip('\n').replace(',', '-').split('-'))
        contains += 1 if (s1 <= s2 and e1 >= e2) or (s2 <= s1 and e2 >= e1) else 0
        overlaps += 1 if not (e1 < s2 or e2 < s1) else 0

print(f'Part A: {contains}')
print(f'Part B: {overlaps}')
