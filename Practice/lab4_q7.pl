solution(V1,V2,V3,H1,H2,H3):-
    word(V1,  _,H1V1,_,H2V1,_,H3V1,_),
    word(H1,  _,H1V1,_,H1V2,_,H1V3,_),
    word(V2,  _,H1V2,_,H2V2,_,H3V2,_),
    word(H2,  _,H2V1,_,H2V2,_,H2V3,_),
    word(V3,  _,H1V3,_,H2V3,_,H3V3,_),
    word(H3,  _,H3V1,_,H3V2,_,H3V3,_).


    word(astante, a,s,t,a,n,t,e). 
    word(astoria, a,s,t,o,r,i,a). 
    word(baratto, b,a,r,a,t,t,o). 
    word(cobalto, c,o,b,a,l,t,o). 
    word(pistola, p,i,s,t,o,l,a). 
    word(statale, s,t,a,t,a,l,e).
    
    test_answer :-
        findall((V1,V2,V3,H1,H2,H3), solution(V1,V2,V3,H1,H2,H3), L),
        sort(L,S), 
        foreach(member(X,S), (write(X), nl)).
    
    test_answer :- write('Wrong answer!').