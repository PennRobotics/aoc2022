from itertools import count

digit_map = {'=': -2, '-': -1, '0': 0, '1': 1, '2': 2}
snafu_map = dict((v,k) for k,v in digit_map.items())

#with open('sample25','r') as file:
bigsum = 0
with open('input25','r') as file:
    #for snafu in ['1=-0-2', '12111', '2=0=', '21', '2=01', '111', '20012', '112', '1=-1=', '1-12', '12', '1=', '122']:
    for snafu in file:
        bigsum += sum([5**n * digit_map[ch] for n,ch in enumerate(reversed(snafu[:-1]))])


for num in [bigsum]:
#for num in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 2022, 12345, 314159265]:
#for num in [1747, 906, 198, 11, 201, 31, 1257, 32, 353, 107, 7, 3, 37]:
    onum = num
    for i in count():
        place = 5**i
        if num // place == 0:
            break
    pad = 2*i
    digs = [0] * pad
    for d in reversed(range(i)):
        place = 5**d
        dig, num = divmod(num, place)
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
    print(onum, digs)
    print(''.join(reversed([snafu_map[dig] for dig in digs])))

print(f'Part A: {0}')
print(f'Part B: {0}')
