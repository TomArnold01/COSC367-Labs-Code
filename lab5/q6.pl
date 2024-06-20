
reverse([],L,L).
reverse([Head|Tail], Accu, Rev) :- reverse(Tail, [Head|Accu], Rev).

splitOddEven([], OddList, EvenList, Odd, Even, _) :- reverse(OddList, [], Odd), reverse(EvenList, [], Even).
splitOddEven([Head|Input], OddList, EvenList, Odd, Even, 0) :- splitOddEven(Input, OddList, [Head|EvenList], Odd, Even, 1).
splitOddEven([Head|Input], OddList, EvenList, Odd, Even, 1) :- splitOddEven(Input, [Head|OddList], EvenList, Odd, Even, 0).

split_odd_even([Head|Input], Odd, Even) :- splitOddEven(Input, [Head|[]], [], Odd, Even, 0).
split_odd_even([], [], []).
