
directlyIn(olga, katarina).
directlyIn(natasha, olga).
directlyIn(irina, natasha).

contains(X,Y):- directlyIn(Y,X).
contains(X,Y):- directlyIn(Y,Z), contains(X,Z).





test_answer :-
    findall(P, contains(P, irina), Output),
    sort(Output, SortedOutput),
    foreach(member(X,SortedOutput), (write(X), nl)).