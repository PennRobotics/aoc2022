class VariablePool:
    def assign(self, var_name, value):
        setattr(self, var_name, value)

varpool = VariablePool()

varpool.assign("test", 42)
print(varpool.test)

dependencies = {}
eval_string = {}
known = {}
with open('sample21', 'r') as file:
    for line in file:
        if any([e in line for e in '+-*/']):
            waiter, waitee_a, waitee_b = line[0:4], line[6:10], line[13:17]
            dependencies[waitee_a] = (waitee_b, waiter)
            dependencies[waitee_b] = (waitee_a, waiter)
            eval_string[waiter] = line[6:].rstrip('\n')
        else:
            known[line[0:4]] = eval(line[6:])

print(eval_string)
print(dependencies)
print(known)

# TODO: while True: search dependencies keys for known, then check if first value is also in dependencies as a key. If yes, run second value's eval string, add to known

print(f'Part A: {0}')
print(f'Part B: {0}')
