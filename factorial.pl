fact(0,1).
fact(1,1).
fact(N,S):-
    N>0,
    N1 is N-1,
    fact(N1,S1),
    S is S1*N.
