same_evens([]).
same_evens([_, S]).
same_evens([_, S|T]):- same_evens(T).



test_answer :-
    same_evens([a, b, c, b, d, b]),
    same_evens([a, b]),
    same_evens([]),
    writeln('OK').


test_answer :-
    same_evens([a, b, c, c, d, b]),
    same_evens([a, b]),
    same_evens([]),
    writeln('OK').