



swap12([_,_], X).
swap12([A, B| Tail], X) :- .


test_answer :-
    swap12([a, b, c, d], L),
    writeln(L).

test_answer :-
    \+ swap12(L, [1]),
    writeln('OK').

test_answer :-
    swap12(L, [b, a]),
    writeln(L).

test_answer :-
    swap12(L1, L2),
    writeln('OK').