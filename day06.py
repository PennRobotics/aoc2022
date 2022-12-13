def search_s_for_n_distinct(s, n):
    i = 0
    while True:
        num_segment_distincts = len(set(line[i:i+n]))
        if num_segment_distincts == n:
            break
        i += n - num_segment_distincts
    return i + n

with open('input06', 'r') as file:
    line = file.read().rstrip('\n')

print(f'Part A: {search_s_for_n_distinct(line, 4)}')
print(f'Part B: {search_s_for_n_distinct(line, 14)}')
