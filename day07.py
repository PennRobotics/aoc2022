fs = dict()

up_one_dir = lambda s: s[-2::-1].split('/', 1)[1][::-1] + '/'

def add_size_along_branch(sz, branch_dir):
    while len(branch_dir) > 1:
        fs[branch_dir] += sz
        branch_dir = up_one_dir(branch_dir)
    fs['/'] += sz
    pass

def construct_fs(in_list):
    pwd = ''
    for line in in_list:
        if '$ ls' in line[0:4]:
            continue
        elif '$ cd' in line[0:4]:
            if line[5:6] == '.' and line[6:7] == '.':
                pwd = up_one_dir(pwd)
            else:
                pwd += line[5:] + '/' if line[5:6] != '/' else '/'
                if pwd not in fs:
                    fs[pwd] = 0
        elif 'dir ' in line[0:4]:
            continue
        else:
            sz_str, fname = line.split(' ')
            sz = int(sz_str)
            fullfname = pwd + fname
            if fullfname not in fs:
                fs[fullfname] = sz
                add_size_along_branch(sz, pwd)
    return fs

with open('input07', 'r') as file:
    contents = file.read().rstrip('\n')

filesystem = construct_fs(contents.split('\n'))

small_dir_sum = 0

free_space = 70000000 - filesystem['/']
space_needed = 30000000 - free_space
smallest_valid_dir_size = 30000000

for k, v in filesystem.items():
    if v > space_needed:
        if v < smallest_valid_dir_size:
            smallest_valid_dir_size = v
    if '/' not in k[-1:] or v > 100000:
        continue
    small_dir_sum += v

print(f'Part A: {small_dir_sum}')
print(f'Part B: {smallest_valid_dir_size}')
