with open('solve12a', 'r') as file:
    contents = file.read().replace('\n', '')
dots = [1*(e == '.') for e in contents]
print(f'Part A: {sum(dots)}')

with open('solve12b', 'r') as file:
    contents = file.read().replace('\n', '')
dots = [1*(e == '.') for e in contents]
print(f'Part B: {sum(dots)}')

# This one was laziness. If prompted, I'd resort to A*
# and create a graph with the next possible directions.
