

new_append([],B, B).

new_append([H|A], B, [H|AB]):- new_append(A, B, AB).



test_answer :-
    new_append([1, 2, 3], [a, b, c], L),
    writeln(L).

test_answer :-
    new_append([1, 2, 3], L, [1, 2, 3, 4, 5]),
    writeln(L).