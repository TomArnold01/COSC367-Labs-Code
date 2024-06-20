remove(out, [], []).
remove(out, [out|T1], Y) :- remove(out, T1, Y).
remove(out, [Head|T1], [Head|T2]) :- remove(out, T1, T2).

