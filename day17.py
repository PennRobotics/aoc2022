DEBUG = print if False else lambda *s: None

from itertools import cycle, count

board = 3*[0]
bricklist = [[0b11110],
             [0b01000, 0b11100, 0b01000],
             [0b11100, 0b00100, 0b00100],
             [0b10000, 0b10000, 0b10000, 0b10000],
             [0b11000, 0b11000]]
brick = cycle(bricklist)

def draw_board(bk, ht):
    out = ''
    n = len(board)
    for row in board[::-1]:
        n -= 1
        buf = '|' + bin(row)[2:].rjust(7, '0').replace('0','.').replace('1','#') + '|\n'
        if n >= ht and n < ht + len(bk):  # Merge block and board characters
            bbuf = '|' + bin(bk[n-ht])[2:].rjust(7, '0').replace('0','.').replace('1','@') + '|\n'
            buf = ''.join([bbuf[i] if bbuf[i] != '.' else buf[i] for i in range(len(buf))])
        out += buf
    out += '+-------+\n'
    print(out)

#with open('sample17', 'r') as file:
with open('input17', 'r') as file:
    jetlist = [1 if jet == '<' else -1 for jet in file.read().rstrip('\n')]
jet = cycle(jetlist)
jet_mod = 0

history = dict()

highest_he = 0
for n in count(1):
    brick_mod = n % 5
    mover = next(brick)
    board = board + [0]*len(mover)
    h = len(board) - len(mover)
    while True:
        #draw_board(mover, h)
        jet_mod = (jet_mod + 1) % len(jetlist)
        if (jet_mod, brick_mod) in history:
            old_h, old_n = history[(jet_mod, brick_mod)]
            dn = n - old_n
            if n % dn == 1000000000000 % dn:
                dh = h - old_h
                n_remaining = 1000000000000 - n
                skips = n_remaining // dn
                print(f'Part B: {skips*dh + h}')
                # 1500874635588 was too high, other Part B answers were off by a few
                # 1500874635585 was too low
                # 1500874635586 was too low. Gee... I wonder what it could be...
                # (In related news, the brick heights probably have something to do with these slightly-off answers.)
        else:
            history[(jet_mod, brick_mod)] = (h, n)
        move = next(jet)
        b_row = board[h:h+len(mover)]
        if move < 0:  # Move right
            proposal = [row if any([r%2 for r in mover]) else row >> 1 for row in mover]
            if any([p & b for p, b in zip(proposal, b_row)]) == 0:  # No collision
                mover = proposal
        else:  # Move left
            proposal = [row if any([r//64 for r in mover]) else row << 1 for row in mover]
            if any([p & b for p, b in zip(proposal, b_row)]) == 0:
                mover = proposal
        #draw_board(mover, h)
        # Fall
        he = h+len(mover)
        impacts = [b & m for b, m in zip(board[h-1:he-1], mover)]
        if any(impacts) == False and h > 0:
            h -= 1
        else:  # Landed
            board[h:he] = [b | m for b, m in zip(board[h:he], mover)]
            highest_he = he if he > highest_he else highest_he
            board = board[:highest_he+3]
            break
    if n == 2022:
        print(f'Part A: {highest_he}')
    if n == 6000000:
        break
    #print(f'Part B: {0}')

