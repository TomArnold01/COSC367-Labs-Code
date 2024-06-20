%listtran([Head|[]], [Trans|[]]) :- tran(Head, Trans).
listtran([], []).
listtran([Head|Tail], [Trans|Ttail]) :- tran(Head, Trans), listtran(Tail, Ttail).