import re


def clauses(knowledge_base):
    """Takes the string of a knowledge base; returns an iterator for pairs
    of (head, body) for propositional definite clauses in the
    knowledge base. Atoms are returned as strings. The head is an atom
    and the body is a (possibly empty) list of atoms.

    -- Kourosh Neshatian - 2 Aug 2021

    """
    ATOM = r"[a-z][a-zA-Z\d_]*"
    HEAD = rf"\s*(?P<HEAD>{ATOM})\s*"
    BODY = rf"\s*(?P<BODY>{ATOM}\s*(,\s*{ATOM}\s*)*)\s*"
    CLAUSE = rf"{HEAD}(:-{BODY})?\."
    KB = rf"^({CLAUSE})*\s*$"

    assert re.match(KB, knowledge_base)

    for mo in re.finditer(CLAUSE, knowledge_base):
        yield mo.group("HEAD"), re.findall(ATOM, mo.group("BODY") or "")


def forward_deduce(knowledge_base):
    inferred_atoms = set()
    knowledge_base = knowledge_base.strip()
    clauses_list = list(clauses(knowledge_base))

    while True:
        new_atoms_added = False
        for head, body_atoms in clauses_list:
            if all(atom in inferred_atoms for atom in body_atoms):
                if head not in inferred_atoms:
                    inferred_atoms.add(head)
                    new_atoms_added = True
        if not new_atoms_added:
            break
    return inferred_atoms


kb = """
a :- b.
b.
"""

print(", ".join(sorted(forward_deduce(kb))))

kb = """
good_programmer :- correct_code.
correct_code :- good_programmer.
"""

print(", ".join(sorted(forward_deduce(kb))))

kb = """
a :- b, c.
b :- d, e.
b :- g, e.
c :- e.
d.
e.
f :- a,
     g.
"""

print(", ".join(sorted(forward_deduce(kb))))
 