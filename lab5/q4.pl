twice([], []).
twice([Head|Tail], [Head, Head|Tail2]) :- twice(Tail, Tail2).