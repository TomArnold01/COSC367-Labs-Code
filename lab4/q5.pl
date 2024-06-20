/* tear rate related clauses */
normal_tear_rate(RATE) :- RATE >= 5.
low_tear_rate(RATE) :- RATE < 5.

/* age-related clauses */
young(AGE) :- AGE < 45.

is_astigmatic(VALUE) :- VALUE = yes.
not_astigmatic(VALUE) :- VALUE = no.

diagnosis(Recommend, Age, Astigmatic, Tear_Rate):- young(Age), normal_tear_rate(Tear_Rate), is_astigmatic(Astigmatic), Recommend = hard_lenses.
diagnosis(Recommend, Age, Astigmatic, Tear_Rate):- young(Age), normal_tear_rate(Tear_Rate), not_astigmatic(Astigmatic), Recommend = soft_lenses.
diagnosis(Recommend, Age, Astigmatic, Tear_Rate):- low_tear_rate(Tear_Rate), Recommend = no_lenses.


test_answer0 :-
    diagnosis(hard_lenses, 21, yes, 11),
    writeln('OK').

test_answer1 :-
    diagnosis(X, 45, no, 4),
    writeln(X).

test_answer2 :-
    diagnosis(X, 19, no, 5),
    writeln(X). 
