from csp import Relation

relations = [Relation(header=['a','b'],
               tuples={(1, -1),
                       (0, 0),
                       (1, 1)}),

      Relation(header=['c', 'd'],
               tuples={(0, -1),
                       (1, -1),
                       (1, 0)}),

      Relation(header=['a', 'b', 'c'],
               tuples={(1, 1, -1),
                       (-1, -1, -1)})
      ] 

relations_after_elimination = [
          Relation(header=['c', 'd'],
               tuples={(0, -1),
                       (1, -1),
                       (1, 0)}),
          
          Relation(header=['b', 'c'],
                   tuples={(1, -1)})
    
    ] 

print(len(relations))
print(all(type(r) is Relation for r in relations))