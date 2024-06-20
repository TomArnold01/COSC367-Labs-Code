import re
from search import *


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


class DFSFrontier(Frontier):
    def __init__(self):
        self.container = []

    def add(self, path):
        self.container.append(path)

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.container) > 0:
            return self.container.pop()
        else:
            raise StopIteration


class KBGraph(Graph):
    def __init__(self, kb, query):
        self.clauses = list(clauses(kb))
        self.query = query

    def starting_nodes(self):
        return [frozenset(self.query)]

    def is_goal(self, node):
        return not node

    def outgoing_arcs(self, tail_node):
        for clause in self.clauses:
            if clause[0] in tail_node:
                new_atoms = set(tail_node)
                new_atoms.discard(clause[0])
                new_atoms.update(clause[1])
                yield Arc(
                    tail_node, frozenset(new_atoms), f"{tail_node} => {new_atoms}", 1
                )


def main():
    kb = """
    a :- c, d.
    c.
    """

    query = {"a"}
    if next(generic_search(KBGraph(kb, query), DFSFrontier()), None):
        print("The query is true.")
    else:
        print("The query is not provable.")

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

    query = {"a"}
    if next(generic_search(KBGraph(kb, query), DFSFrontier()), None):
        print("The query is true.")
    else:
        print("The query is not provable.")

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

    query = {"a", "b", "d"}
    if next(generic_search(KBGraph(kb, query), DFSFrontier()), None):
        print("The query is true.")
    else:
        print("The query is not provable.")

    kb = """
    all_tests_passed :- program_is_correct.
    all_tests_passed.
    """

    query = {"program_is_correct"}
    if next(generic_search(KBGraph(kb, query), DFSFrontier()), None):
        print("The query is true.")
    else:
        print("The query is not provable.")

    kb = """
    a :- b.
    """

    query = {"c"}
    if next(generic_search(KBGraph(kb, query), DFSFrontier()), None):
        print("The query is true.")
    else:
        print("The query is not provable.")


if __name__ == "__main__":
    main()
