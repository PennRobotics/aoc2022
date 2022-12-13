LOSE = 0; TIE = 3; WIN = 6

score = 0
shape_points = {'X': 1, 'Y': 2, 'Z': 3}
outcome_points = {
        'A': {'X': TIE,  'Y': WIN,  'Z': LOSE},
        'B': {'X': LOSE, 'Y': TIE,  'Z': WIN },
        'C': {'X': WIN,  'Y': LOSE, 'Z': TIE } }

def cmp(a, b):
    return (a > b) - (a < b)

with open('input02', 'r') as file:
    contents = file.read().rstrip('\n')
pairs = contents.split('\n')

for pair in pairs:
    l, r = pair.split(' ')
    score += shape_points[r]
    score += outcome_points[l][r]

print(f'Part A: {score}')

score = 0
decoder = {'X': {'A': 3+LOSE, 'B': 1+LOSE, 'C': 2+LOSE},  # Lose
           'Y': {'A': 1+TIE,  'B': 2+TIE,  'C': 3+TIE },  # Draw
           'Z': {'A': 2+WIN,  'B': 3+WIN,  'C': 1+WIN } }  # Win

for pair in pairs:
    l, r = pair.split(' ')
    score += decoder[r][l]

print(f'Part B: {score}')
