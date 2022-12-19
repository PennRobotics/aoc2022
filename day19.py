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
    blueprints = [re.findall(r'\d+', l) for l in file.read().rstrip('\n').split('\n')]

best_score = 0
possible_states = []
for bid, C1o, C2o, C3o, C3c, C4o, C4c in blueprints:
    mn, score, job, no, nc, nobs, ng, n1, n2, n3, n4 = 2, -1, NOTHING, 2, 0, 0, 0, 1, 0, 0, 0
    state = [bid, mn, score, job, no, nc, nobs, ng, n1, n2, n3, n4]
    possible_states.append(state)

    candidate_state = copy(state)
    candidate_state[1] += MINUTE

    candidate_state[4] += n1
    candidate_state[5] += n2
    candidate_state[6] += n3
    candidate_state[7] += n4

    # TODO: add candidate states for each type of build option (nothing or robot)
    # TODO: check if the candidate state is feasible (can a geode robot be build by 23m?) or even optimal (how many geode robots COULD be built given a set of inputs?)
    # TODO: choose top state, go to next blueprint

    best_state = possible_states[0]
    for examined_state in possible_states:
        best_state = state if score > best_score else best_state
        best_score = score if score > best_score else best_score

    DEBUG(bid, C1o)

DEBUG(blueprints)

print(f'Part A: {0}')
print(f'Part B: {0}')
