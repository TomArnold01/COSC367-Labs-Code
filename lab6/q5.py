from csp import Relation

relations = [
    Relation(header=['a','b','c'],
            tuples={(2, 0, 1),
                    (2, 1, 0),
                    (1, 0, 0),
                    (2, 0, 0)
                   }),

    Relation(header=['c','d'],
            tuples={(1,0),
                    (2,0),
                    (2,1)
            })

]


print(len(relations))
print(all(type(r) is Relation for r in relations))
print(sorted(sorted(relations)[0].tuples))