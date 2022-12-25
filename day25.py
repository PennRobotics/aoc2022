from itertools import count

digit_map = {'=': -2, '-': -1, '0': 0, '1': 1, '2': 2}
snafu_map = dict((v,k) for k,v in digit_map.items())

bigsum = 0
with open('input25','r') as file:
    for snafu in file:
        bigsum += sum([5**n * digit_map[ch] for n,ch in enumerate(reversed(snafu[:-1]))])

for i in count():
    place = 5**i
    if bigsum // place == 0:
        break
pad = 2*i
digs = [0] * pad
for d in reversed(range(i)):
    place = 5**d
    dig, bigsum = divmod(bigsum, place)
    digs[d] += dig
    for scan in range(d,i):
        if digs[scan] > 2:
            digs[scan] -= 5
            digs[scan+1] += 1
while True:
    pad -= 1
    if digs[pad] != 0:
        break
    del digs[pad]

print(f'Part A: {"".join(reversed([snafu_map[dig] for dig in digs]))}')
print(f'Part B: {0}')
