DEBUG = print if True else lambda *s: None

import re
from copy import copy

NOTHING        = 0
ORE_ROBOT      = 1
CLAY_ROBOT     = 2
OBSIDIAN_ROBOT = 4
GEODE_ROBOT    = 8

MINUTE = 1

#with open('sample19', 'r') as file:
with open('input19', 'r') as file:
    blueprints = [map(int, re.findall(r'\d+', l)) for l in file.read().rstrip('\n').split('\n')]

best_score = 0
possible_states = []
for bid, C1o, C2o, C3o, C3c, C4o, C4c in blueprints:
    job, no, nc, nobs, ng, n1, n2, n3, n4 = NOTHING, 0, 0, 0, 0, 1, 0, 0, 0
    state = [bid, job, no, nc, nobs, ng, n1, n2, n3, n4]
    possible_states.append([0] + state)
    for mn in range(1, 24+1):
        # max_ore_robots = 1 + first_criteria + second_criteria + third_criteria (saturated, divide remaining minutes by num of robots)
        # max_clay_robots = first_criteria + second_criteria + ... (worst case is eleven for blueprint 24, saturation here is 10)
        # max_geode_robots = some sort of triangle number thing, or (absolute most naive) ~21 minus fib number leading to x obsidian
        # max_obsidian_robots = should be able to back out the earliest robot using previous two, enumerate all cases and test individually

        state[2] += n1
        state[3] += n2
        state[4] += n3
        state[5] += n4

        candidate_state = [mn] + copy(state)

        DEBUG(n1)
        possible_states.append(candidate_state)

    # TODO: add candidate states for each type of build option (nothing or robot)
    # TODO: check if the candidate state is feasible (can a geode robot be build by 23m?) or even optimal (how many geode robots COULD be built given a set of inputs?)
    # TODO: choose top state, go to next blueprint

    DEBUG(possible_states)
    DEBUG('\n'.join([', '.join([str(e) for e in v]) for v in possible_states]))

    best_state = possible_states[0]
    for examined_state in possible_states:
        score = 0
        best_state = state if score > best_score else best_state
        best_score = score if score > best_score else best_score
    break

print(f'Part A: {0}')
print(f'Part B: {0}')
