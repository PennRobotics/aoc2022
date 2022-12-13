with open('solve12a', 'r') as file:
    contents = file.read().replace('\n', '')
dots = [1*(e == '.') for e in contents]
print(f'Part A: {sum(dots)}')

with open('solve12b', 'r') as file:
    contents = file.read().replace('\n', '')
dots = [1*(e == '.') for e in contents]
print(f'Part B: {sum(dots)}')

