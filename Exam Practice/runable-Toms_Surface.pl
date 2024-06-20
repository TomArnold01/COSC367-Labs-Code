

leaves(tree([Leaf|Rest]), [Leaf|Leaves]) :-
    atom(Leaf),
    leaves(tree(Rest), Leaves).

leaves(tree([Subtree|Rest]), Leaves) :-
    \+ atom(Subtree),
    leaves(Subtree, SubtreeLeaves),
    leaves(tree(Rest), RestLeaves),
    append(SubtreeLeaves, RestLeaves, Leaves).

leaves(_, []).



test_answer :- leaves(tree([the_only_leaf]), Leaves),
               writeln(Leaves).

            
test_answer :- leaves(tree([a, tree([b,c,d])]), L),
               writeln(L).

