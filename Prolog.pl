eats(Name,Thing) :- likes(Name,Thing).
eats(Name, Thing) :- edible(Thing), hungry(Name).
/* ------------------------------------------------------------------------------------------------------------------------- */
reflection(point(X,Y), point(Y,X)).
/* ------------------------------------------------------------------------------------------------------------------------- */
/* tear rate related clauses */
normal_tear_rate(RATE) :- RATE >= 5.
low_tear_rate(RATE) :- RATE < 5.

/* age-related clauses */
young(AGE) :- AGE < 45.

/* recommend clauses */
soft(RECOMMEND) :- RECOMMEND = soft_lenses.
hard(RECOMMEND) :- RECOMMEND = hard_lenses.
no_lenses(RECOMMEND) :- RECOMMEND = no_lenses.

diagnosis(Recommend, Age, Astigmatic, Tear_Rate) :-
young(Age), normal_tear_rate(Tear_Rate), soft(Recommend).

diagnosis(Recommend, Age, Astigmatic, Tear_Rate) :- 
young(Age), normal_tear_rate(Tear_Rate), hard(Recommend).

diagnosis(Recommend, Age, Astigmatic, Tear_Rate) :- 
low_tear_rate(Tear_Rate), no_lenses(Recommend).
/* ------------------------------------------------------------------------------------------------------------------------- */
directlyIn(olga, katarina).
directlyIn(natasha, olga).
directlyIn(irina, natasha).

contains(X, Y) :- directlyIn(Y, X).
contains(X, Y) :- directlyIn(Y, Z), contains(X, Z).
/* ------------------------------------------------------------------------------------------------------------------------- */
crossword(V1, V2, V3, H1, H2, H3) :- word(V1, _,O,_,R,_,U,_), word(V2, _,P,_,S,_,V,_), word(V3, _,Q,_,T,_,W,_),
                                     word(H1, _,O,_,P,_,Q,_), word(H2, _,R,_,S,_,T,_), word(H3, _,U,_,V,_,W,_).                                     
/* ------------------------------------------------------------------------------------------------------------------------- */
mirror(leaf(X), leaf(X)).
mirror(tree(A1,B1), tree(A2,B2)) :- mirror(A2, B1), mirror(A1, B2).
/* ------------------------------------------------------------------------------------------------------------------------- */
second([X,Y|L],Y).
/* ------------------------------------------------------------------------------------------------------------------------- */
swap12([X,Y|T],[Y,X|T]).
/* ------------------------------------------------------------------------------------------------------------------------- */
listtran([],[]).
listtran([Hg|Tg],[He|Te]) :- tran(Hg,He), listtran(Tg,Te).
/* ------------------------------------------------------------------------------------------------------------------------- */
twice([],[]).
twice([H1|T1],[H1, H1|T2]) :- twice(T1,T2).
/* ------------------------------------------------------------------------------------------------------------------------- */
swap_ends([],[]).
swap_ends(L1, L2):-append([H|M],[T],L1), append([T|M],[H],L2).
/* ------------------------------------------------------------------------------------------------------------------------- */
addone([],[]).
addone([H|T1],[N|T2]) :- N is H+1, addone(T1, T2).
/* ------------------------------------------------------------------------------------------------------------------------- */
element([H|_],0,H).
element([_|T],N,X) :- element(T,K,X), N is K+1.
/* ------------------------------------------------------------------------------------------------------------------------- */
remove(X,[],[]).
remove(A,[A|T],L):-remove(A,T,L).
remove(A,[B|T],[B|L]):-remove(A,T,L).
/* ------------------------------------------------------------------------------------------------------------------------- */
split_odd_even([],[],[]).
split_odd_even([X],[X],[]).
split_odd_even([X,Y|T],[X|Odd],[Y|Even]):-split_odd_even(T,Odd,Even).
/* ------------------------------------------------------------------------------------------------------------------------- */
merge([],[],[]).
merge([],X,X).
merge(X,[],X).
merge([X|Tx],[Y|Ty],[X|L]):-X=<Y, merge(Tx,[Y|Ty],L).
merge([X|Tx],[Y|Ty],[Y|L]):-Y=<X, merge([X|Tx],Ty,L).
/* ------------------------------------------------------------------------------------------------------------------------- */
split_odd_even([],[],[]).
split_odd_even([X],[X],[]).
split_odd_even([X,Y|T],[X|Odd],[Y|Even]):-split_odd_even(T,Odd,Even).

merge([],[],[]).
merge([],X,X).
merge(X,[],X).
merge([X|Tx],[Y|Ty],[X|L]):-X=<Y, merge(Tx,[Y|Ty],L).
merge([X|Tx],[Y|Ty],[Y|L]):-Y=<X, merge([X|Tx],Ty,L).

merge_sort([], []).
merge_sort([X], [X]).
merge_sort(In, Out) :- split_odd_even(In, OddList, EvenList), merge_sort(OddList, Odd), merge_sort(EvenList, Even), merge(Odd, Even, Out).
/* ------------------------------------------------------------------------------------------------------------------------- */
inside(A,B,C) :- A=<B,C=A.
inside(A,B,C) :- A < B, X is A+1, inside(X,B,C).
/* ------------------------------------------------------------------------------------------------------------------------- */
py_triple(A,B,C) :-  0 < A, A =< B, B =< C, C2 is C*C, AB is A*A+B*B, C2 = AB.
/* ------------------------------------------------------------------------------------------------------------------------- */
inside(A,B,C) :- A=<B,C=A.
inside(A,B,C) :- A < B, X is A+1, inside(X,B,C).

py_triple(A,B,C) :-  0 < A, A =< B, B =< C, C2 is C*C, AB is A*A+B*B, C2 = AB.

py_triple(A,B,C,Min,Max):-inside(Min,Max,A), inside(Min,Max,B), inside(Min,Max,C), py_triple(A,B,C).
/* ------------------------------------------------------------------------------------------------------------------------- */
