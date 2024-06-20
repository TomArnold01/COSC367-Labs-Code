import itertools

def interpretations(atoms):
    values = [False, True]
    result = []

    for combo in itertools.product(values, repeat=len(atoms)):
        pair = dict(zip(sorted(atoms), combo))
        result.append(pair)

    return result





atoms = {'a', 'b', 'c'}
for i in interpretations(atoms):
    print(i)

# atoms = {'human', 'mortal', 'rational'}
# for i in interpretations(atoms):
#     print(i)