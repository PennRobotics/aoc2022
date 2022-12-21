class VariablePool:
    def assign(self, var_name, eval_str):
        mod_eval_str = 'self.' + eval_str[0:7] + 'self.' + eval_str[7:]
        setattr(self, var_name, eval(mod_eval_str))

varpool = VariablePool()

while False:
    dependencies = {}
    eval_string = {}
    known = {}
    with open('input21', 'r') as file:
        for line in file:
            if any([e in line for e in '+-*/']):
                waiter, waitee_a, waitee_b = line[0:4], line[6:10], line[13:17]
                dependencies[waitee_a] = (waitee_b, waiter)
                dependencies[waitee_b] = (waitee_a, waiter)
                eval_string[waiter] = line[6:].rstrip('\n')
            else:
                key = line[0:4]
                val = eval(line[6:])
                known[key] = val
                setattr(varpool, key, val)

    while dependencies:
        dep_list = list(dependencies.items())
        deleted = []
        for dep, (other_dep, assign_var) in dep_list:
            if dep not in known or other_dep not in known or assign_var in deleted:
                continue

            varpool.assign(assign_var, eval_string[assign_var])
            known[assign_var] = getattr(varpool, assign_var)

            del dependencies[dep]
            del dependencies[other_dep]
            del eval_string[assign_var]
            deleted.append(assign_var)

    root = int(getattr(varpool, "root"))

    print(f'Part A: {root}')


# Part B
dependencies = {}
eval_string = {}
known = {}
with open('input21', 'r') as file:
    for line in file:
        if any([e in line for e in '+-*/']):  ### or not 'humn' in line[0:4]:
            ### if 'root' in line[0:4]:
                ### continue
            waiter, waitee_a, waitee_b = line[0:4], line[6:10], line[13:17]
            dependencies[waitee_a] = (waitee_b, waiter)
            dependencies[waitee_b] = (waitee_a, waiter)
            eval_string[waiter] = line[6:].rstrip('\n')
        else:
            ### if 'humn' in line[0:4]:
                ### line = 'humn: 3090000000000'
                ### print(line)
            key = line[0:4]
            val = eval(line[6:])
            known[key] = val
            setattr(varpool, key, val)

while dependencies:
    dep_list = list(dependencies.items())
    #print(len(dep_list), flush=True)
    deleted = []
    for dep, (other_dep, assign_var) in dep_list:
        if dep not in known or other_dep not in known or assign_var in deleted:
            continue

        varpool.assign(assign_var, eval_string[assign_var])
        known[assign_var] = getattr(varpool, assign_var)

        del dependencies[dep]
        del dependencies[other_dep]
        del eval_string[assign_var]
        deleted.append(assign_var)

lttc = getattr(varpool, "lttc")
pfjc = getattr(varpool, "pfjc")
root = getattr(varpool, "root")

print(f'Part B: {root/2}  {lttc}  {pfjc}  {pfjc-lttc}')
