
reversed([],[]).

reversed([Head|Tail], Backward):- reversed(Tail, ReversedTail), 
                append(ReversedTail, [Head], Backward).

test_answer :- 
    reversed([1, 2, 3, 4, 5], L),
    writeln(L).

test_answer :- 
    reversed(L, [d, c, b, a]),
    writeln(L).