digit_map = {'=': -2, '-': -1, '0': 0, '1': 1, '2': 2}

#with open('sample25','r') as file:
#with open('input25','r') as file:
for snafu in ['1=-0-2', '12111', '2=0=', '21', '2=01', '111', '20012', '112', '1=-1=', '1-12', '12', '1=', '122']:
    print(sum([5**n * digit_map[ch] for n,ch in enumerate(reversed(snafu))]))

print(f'Part A: {0}')
print(f'Part B: {0}')
