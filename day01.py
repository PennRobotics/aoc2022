with open('input01', 'r') as file:
    contents = file.read().rstrip('\n')
groups = contents.split('\n\n')
splitgroups = (g.split('\n') for g in groups)
sums = []
for thisgroup in splitgroups:
    sums.append(sum((int(e) for e in thisgroup)))
sums.sort()
print(f'Part A: {sums[-1]}')
print(f'Part B: {sum(sums[-3:])}')

