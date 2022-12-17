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

with open('sample17', 'r') as file:
#with open('input17', 'r') as file:
    jetlist = [1 if jet == '<' else -1 for jet in file.read().rstrip('\n')]
jet = cycle(jetlist)

highest_he = 0
for n in count(1):
    mover = next(brick)
    board = board + [0]*len(mover)
    h = len(board) - len(mover)
    while True:
        #draw_board(mover, h)
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
        break

print(f'Part A: {highest_he}')
print(f'Part B: {0}')
