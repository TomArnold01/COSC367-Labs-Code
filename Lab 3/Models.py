import itertools

def atoms(formula):
    """Takes a formula in the form of a lambda expression and returns a set of
    atoms used in the formula. The atoms are parameter names represented as
    strings.
    """
    
    return {atom for atom in formula.__code__.co_varnames}
    
def value(formula, interpretation):
    """Takes a formula in the form of a lambda expression and an interpretation
    in the form of a dictionary, and evaluates the formula with the given
    interpretation and returns the result. The interpretation may contain
    more atoms than needed for the single formula.
    """
    arguments = {atom: interpretation[atom] for atom in atoms(formula)}
    return formula(**arguments)

def interpretations(atoms):
    values = [False, True]
    result = []

    for combo in itertools.product(values, repeat=len(atoms)):
        pair = dict(zip(sorted(atoms), combo))
        result.append(pair)

    return result

def models(knowledge_base):
    all_atoms = set()
    for formula in knowledge_base:
        all_atoms.update(atoms(formula))
    all_interpretations = interpretations(all_atoms)

    valid_models = []
    for interpretation in all_interpretations:
        is_valid = all(value(formula, interpretation) for formula in knowledge_base)
        if is_valid:
            valid_models.append(interpretation)

    return valid_models

knowledge_base = {
    lambda a, b: a and not b,
    lambda c, d: c or d
}

for interpretation in models(knowledge_base):
    print(interpretation)


knowledge_base = {
    lambda a, b: a and not b,
    lambda c: c
}

print(models(knowledge_base))
