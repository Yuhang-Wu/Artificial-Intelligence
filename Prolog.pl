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

diagnosis(Recommend, Age, Astigmatic, Tear_Rate) :- young(Age), normal_tear_rate(Tear_Rate), soft(Recommend).

diagnosis(Recommend, Age, Astigmatic, Tear_Rate) :- young(Age), normal_tear_rate(Tear_Rate), hard(Recommend).

diagnosis(Recommend, Age, Astigmatic, Tear_Rate) :- low_tear_rate(Tear_Rate), no_lenses(Recommend).

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

merge_sort([],[]).
merge_sort([X],[X]).
merge_sort(In,Out) :- split_odd_even(In,OddList,EvenList), merge_sort(OddList,Odd), merge_sort(EvenList,Even), merge(Odd,Even,Out).

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
% Write a predicate binary_number(+ListOfAtoms) that only succeeds if the given list of atoms is a valid binary number. 
% We consider a binary number valid if it matches the following regex: 0b(0|(1(0|1)*)).

binary_number([]).
binary_number([0, b, 0]).
binary_number([0, b, 1 | T]) :- binary_number(0b1, T).
binary_number(0b1, [H|T]) :- H=0; H=1, binary_number(0b1, T).

/* ------------------------------------------------------------------------------------------------------------------------- */
% Write a predicate product(+Numbers, Product) that calculates the product of a list of numbers. 
% If the list is empty, the product is 1.

product([],1).
product([H|T],N):- product(T,K), N is K*H.

/* ------------------------------------------------------------------------------------------------------------------------- */
% DNA is a really big molecule that encodes all the information about an organism. 
% It has four bases: cytosine (c), guanine (g), adenine (a), and thymine (t). 
% Base c always pairs with g, and a always pairs with t, 
% meaning that from a single half of a DNA strand you can always build the other: 
% this is exactly what your body does when cells are splitting! 

% Write a predicate dna(?Left, ?Right) that makes sure the left and right halves of a DNA strand match.

match(c,g).
match(g,c).
match(a,t).
match(t,a).

dna([],[]).
dna([Hl|Tl],[Hr|Tr]):-match(Hl,Hr),dna(Tl,Tr).

/* ------------------------------------------------------------------------------------------------------------------------- */
% Write a predicate new_append(?A, ?B, ?AB) that behaves exactly the same as the built-in append/3, without using append/3.

new_append([],X,X).
new_append([Ha|Ta],B,[Ha|AB]):- new_append(Ta,B,AB).

/* ------------------------------------------------------------------------------------------------------------------------- */

reversed([],Acc,Acc).
reversed([Hx|Tx],Acc,Y):-reversed(Tx,[Hx|Acc],Y).
reversed(X,Y) :- reversed(X,[],Y).

/* ------------------------------------------------------------------------------------------------------------------------- */
% Write a predicate preorder(+Tree, Traversal) that determines the preorder traversal of a given binary tree. 
% Each tree/subtree is either a leaf or of the form tree(root, left_subtree, right_subtree). 
% A preorder traversal records the current node, then the left branch, then the right branch.
% preorder(leaf(a), L). --> L = [a].
% preorder(tree(a, tree(b, leaf(c), leaf(d)), leaf(e)), T). --> T = [a,b,c,d,e].

preorder(leaf(X),[X]).
preorder(tree(Root,L,R),[Root|T]):-preorder(L,TL),preorder(R,TR),append(TL,TR,T).

/* ------------------------------------------------------------------------------------------------------------------------- */
% Write a predicate postorder(+Tree, Traversal) that determines the postorder traversal of a given binary tree. 
% Each tree/subtree is either a leaf or of the form tree(root, left_subtree, right_subtree).
% A postorder traversal records the left branch, then the right branch, then the current node.

postorder(leaf(X),[X]).
postorder(tree(Root,L,R),T):-postorder(L,TL),postorder(R,TR),append(TL,TR,TLR),append(TLR,[Root],T).

/* ------------------------------------------------------------------------------------------------------------------------- */
% Define a predicate fib(+N, Numbers) that produces the first N Fibonacci numbers. 
% We will never ask for less than two numbers.

fib(2,[0,1]).
fib(N,X):- K is N-1, fib(K,Nums), reverse(Nums,[A,B|_]), Var is A+B, append(Nums,[Var],X).

/* ------------------------------------------------------------------------------------------------------------------------- */
% Write a predicate rle(+LongForm, ShortForm) that creates the run-length encoding of the LongForm list.
% rle([a, a, b, c, c, c], X). --> X = [(a,2), (b,1), (c,3)].

rle([],[]).
rle([X|Xs],[Z|Zs]) :- count(X,Xs,Ys,1,Z), rle(Ys,Zs).

count(X,[],[],1,(X,1)).
count(X,[],[],N,(X,N)) :- N > 1.

count(X,[Y|Ys],[Y|Ys],1,(X,1)) :- X \= Y.
count(X,[Y|Ys],[Y|Ys],N,(X,N)) :- N > 1, X \= Y.
count(X,[X|Xs],Ys,K,T) :- K1 is K + 1, count(X,Xs,Ys,K1,T).

/* Anoter way to solve it */

encode(L1,L2) :- pack(L1,L), transform(L,L2).

transform([],[]).
transform([[X|Xs]|Ys],[(X,N)|Zs]) :- length([X|Xs],N), transform(Ys,Zs).

pack([],[]).
pack([X|Xs],[Z|Zs]) :- transfer(X,Xs,Ys,Z), pack(Ys,Zs).

transfer(X,[],[],[X]).
transfer(X,[Y|Ys],[Y|Ys],[X]) :- X \= Y.
transfer(X,[X|Xs],Ys,[X|Zs]) :- transfer(X,Xs,Ys,Zs).

/* ------------------------------------------------------------------------------------------------------------------------- */
% Write a predicate cartesian_product(?A, ?B, ?AcrossB) that forms the cartesian product of two lists.
% The cartesian product is all possible pairings of elements from the two lists.
% Hint: it might be a good idea to define a "helper" predicate that pairs a single element X with every element in a List.

helper(A,[],[]).
helper(A,[H|T],[(A,H)|AB]) :- helper(A,T,AB).

cartesian_product([],X,[]).
cartesian_product(X,[],[]).
cartesian_product([H|T],B,AB):-helper(H,B,AB1), cartesian_product(T,B,AB2), append(AB1,AB2,AB).
