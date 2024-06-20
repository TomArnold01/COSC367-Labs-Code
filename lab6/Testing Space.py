import itertools, copy 
from csp import scope, satisfies, CSP

def arc_consistent(csp):
    csp = copy.deepcopy(csp)
    to_do = {(x, c) for c in csp.constraints for x in scope(c)} # COMPLETE
    while to_do:
        x, c = to_do.pop()
        ys = scope(c) - {x}
        new_domain = set()
        for xval in csp.var_domains[x]: # COMPLETE
            assignment = {x: xval}
            for yvals in itertools.product(*[csp.var_domains[y] for y in ys]):
                assignment.update({y: yval for y, yval in zip(ys, yvals)})
                if satisfies(assignment, c): # COMPLETE
                    new_domain.add(xval) # COMPLETE
                    break
        if csp.var_domains[x] != new_domain:
            for cprime in set(csp.constraints) - {c}:
                if x in scope(cprime):
                   for z in scope(cprime): # COMPLETE
                       if x != z: # COMPLETE
                           to_do.add((z, cprime))
            csp.var_domains[x] = new_domain     #COMPLETE
    return csp
    
def generate_and_test(csp):
    names, domains = zip(*csp.var_domains.items())
    for values in itertools.product(*domains):
        assignment = {x: v for x, v in zip(names, values)}
        if all(satisfies(assignment, c) for c in csp.constraints):
            yield assignment

domains = {x: set(range(10)) for x in "twofur"}
domains.update({'c1':{0, 1}, 'c2': {0, 1}}) # domains of the carry overs

cryptic_puzzle = CSP(
    var_domains=domains,
    constraints={
        lambda o, r, c1 : o + o == r + 10 * c1, 
        lambda w, u, c1, c2 : w + w + c1 == u + 10 * c2,
        lambda t, o, c2 : t + t + c2 == o + 10,
        lambda f : f == 1,
        lambda t, w, o, f, u, r : len({t, w, o, f, u, r}) > 5,
        })


print(set("twofur") <= set(cryptic_puzzle.var_domains.keys()))
print(all(len(cryptic_puzzle.var_domains[var]) == 10 for var in "twofur"))

new_csp = arc_consistent(cryptic_puzzle)
print(sorted(new_csp.var_domains['r']))

new_csp = arc_consistent(cryptic_puzzle)
print(sorted(new_csp.var_domains['w']))


new_csp = arc_consistent(cryptic_puzzle)
solutions = []
for solution in generate_and_test(new_csp):
    solutions.append(sorted((x, v) for x, v in solution.items()
                            if x in "twofur"))
print(len(solutions))
solutions.sort()
print(solutions[0])
print(solutions[5])