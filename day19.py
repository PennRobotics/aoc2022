DEBUG = print if True else lambda *s: None

import re
from copy import deepcopy

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
for bid, C1o, C2o, C3o, C3c, C4o, C4x in blueprints:
    job, no, nc, nx, ng, n1, n2, n3, n4 = NOTHING, 0, 0, 0, 0, 1, 0, 0, 0
    state = [0, job, no, nc, nx, ng, n1, n2, n3, n4]
    possible_states.append(deepcopy(state))
    del state
    for mn in range(1, 5+1):
        print(mn,flush=True)
        # max_ore_robots = 1 + first_criteria + second_criteria + third_criteria (saturated, divide remaining minutes by num of robots)
        # max_clay_robots = first_criteria + second_criteria + ... (worst case is eleven for blueprint 24, saturation here is 10)
        # max_geode_robots = some sort of triangle number thing, or (absolute most naive) ~21 minus fib number leading to x obsidian
        # max_obsidian_robots = should be able to back out the earliest robot using previous two, enumerate all cases and test individually

        #for i, state in enumerate(possible_states):
        #    if state[0] < mn - 2:
        #        continue
        #    possible_states = possible_states[i:]

        current_state_len = len(possible_states)
        for i in range(current_state_len):
            state = deepcopy(possible_states[i])

            job, no, nc, nx, ng, n1, n2, n3, n4 = state[1:10]

            #DEBUG('+', state)

            state[0] += MINUTE

            state[2] += n1
            state[3] += n2
            state[4] += n3
            state[5] += n4

            state[5:9] = n1+(job==ORE_ROBOT), n2+(job==CLAY_ROBOT), n3+(job==OBSIDIAN_ROBOT), n4+(job==GEODE_ROBOT)

            #DEBUG('+', state)
            if nx >= C4x and no >= C4o:
                state[1] = GEODE_ROBOT  # Greedy creation of geodes
            elif nc >= C3c and no >= C3o and n3 < C4x:
                state[1] = OBSIDIAN_ROBOT  # Greedy creation of obsidian
            else:
                state[1] = NOTHING
            candidate_state = deepcopy(state)
            possible_states.append(candidate_state)

            if n1 < max(C1o, C2o, C3o, C4o):  # Saturation (cannot create more than one bot per turn for any material)
                state[1] = ORE_ROBOT
                candidate_state = deepcopy(state)
                possible_states.append(candidate_state)

            if n2 < C3c:  # Saturation
                state[1] = CLAY_ROBOT
                candidate_state = deepcopy(state)
                possible_states.append(candidate_state)

    # TODO: add candidate states for each type of build option (nothing or robot)
    # TODO: check if the candidate state is feasible (can a geode robot be build by 23m?) or even optimal (how many geode robots COULD be built given a set of inputs?)
    # TODO: choose top state, go to next blueprint
    # TODO: if it's easy to check and time permits, get min and max bounds for ore and clay, figure out if there's a predictable ratio between each type of material, etc.

            #DEBUG(possible_states)
            #DEBUG('\n'.join([', '.join([str(e) for e in v]) for v in possible_states]))

            #best_state = possible_states[0]
            #for examined_state in possible_states:
                #score = 0
                #best_state = state if score > best_score else best_state
                #best_score = score if score > best_score else best_score

print(f'Part A: {0}')
print(f'Part B: {0}')

# Hand calculation of #2:  (seemingly low-production case)
'''
build 2 ore bots, clay almost every turn (6)
build 10 clay (18)
obs almost every turn
basically 1 geode bot, if that, and certainly late

OR

build 1 ore bot, clay every other turn (3)
build 7 clay (17)
obs every other turn
maybe 2 geode bots? maybe even still zero?

1 robot = 2 ore + 16 obsidian = 2 ore + 16*(4 ore + 14 clay) = 64 ore + 224*(4 ore) = 960 ore-equivalent

16 obsidian is 1+1+2+2+3+3+4 (obs every other turn), obs 1+2+3+4+4 clay,

Trying again:
after 4, 2b. After 6, 3b. After 8, 4b., After 12, 4c. After 13, 1x, @14,5c,@15,6c,@17,7c/2x,@19,3x,@22 maybe a geode bot

'''

# Hand calculation of #24:  (seemingly high-production case)
'''
build new ore robot, clay robots can be built every turn (3)
with 5 clay robots, an obs robot can be built every other turn (8)
a surplus of ore will build (avg 1 per turn)
in the between turns, one of the others could be built and might help production
with 4 obs robots, a geode robot should be buildable every 3 turns (16)
1 geode somewhere between 13 and 15 (
2 around 17
3 around 20
4 around 23 [3+6+9+4 = 22 hopefully, and probably a few more]
'''
