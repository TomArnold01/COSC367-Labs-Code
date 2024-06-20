import re










def clauses(knowledge_base):
    """Takes the string of a knowledge base; returns an iterator for pairs
    of (head, body) for propositional definite clauses in the
    knowledge base. Atoms are returned as strings. The head is an atom
    and the body is a (possibly empty) list of atoms.

    -- Kourosh Neshatian - 2 Aug 2021

    """
    ATOM   = r"[a-z][a-zA-Z\d_]*"
    HEAD   = rf"\s*(?P<HEAD>{ATOM})\s*"
    BODY   = rf"\s*(?P<BODY>{ATOM}\s*(,\s*{ATOM}\s*)*)\s*"
    CLAUSE = rf"{HEAD}(:-{BODY})?\."
    KB     = rf"^({CLAUSE})*\s*$"

    assert re.match(KB, knowledge_base)

    for mo in re.finditer(CLAUSE, knowledge_base):
        yield mo.group('HEAD'), re.findall(ATOM, mo.group('BODY') or "")

def forward_deduce(kb):
    test = list(clauses(kb))
    known = []

    for item in test:
        for i in item:
            if type(i) == str:
                if len(i) == 1:
                    known.append(i)
            elif type(i) == list:
                for char in i:
                    if type(i) == str:
                        if len(i) == 1:
                            known.append(i)
    return known



def main():

    kb = """
    a :- b.
    b.
    """

    print(forward_deduce(kb))

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

if __name__ == "__main__":
    main()

