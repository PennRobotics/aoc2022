DEBUG = print if False else lambda *s: None

bricks = [[0b1111],
          [0b010, 0b111, 0b010],
          [0b001, 0b001, 0b111],
          [0b1, 0b1, 0b1, 0b1],
          [0b11, 0b11]]

with open('input17', 'r') as file:
    jets = [1 if jet is '<' else -1 for jet in file.read().rstrip('\n')]

board = [0] * 4

print(f'Part A: {0}')
print(f'Part B: {0}')
