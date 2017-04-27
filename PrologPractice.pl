/* find the last element */
theLast([X],X).
theLast([_|L],X) :- theLast(L, X).

/* find the last but one leement */
last_but_one([X,_|[]], X).
last_but_one([_,S|T], X) :- last_but_one([S|T], X).

/* find the K'th element of a list. the index of the first element is 0 */
element_at([H|_],0,H).
element_at([_|T],Index,H) :- element(T,I,H), Index is I+1.

/* find the number of elements in th elist */
elementNum([],0).
elementNum([_|T], Num) :- elementNum(T,N), Num is N+1.

list_len([], Acc, Acc).
list_len([_|T], OldAcc, Len) :- NewAcc is OldAcc + 1, list_len(T, NewAcc, Len).
list_len(L, Len):- list_len(L, 0, Len).

/* reverse a list */
revAcc([], Acc, Acc).
revAcc([H|T], OldAcc, L2) :- revAcc(T, [H|OldAcc], L2).
revAcc(L1, L2) :- revAcc(L1, [], L2).

/* check wether a list is a palindrome */
palindrome(L) :- revAcc(L,L).

/* duplicate the elements of a list */
duplicate([], []).
duplicate([H|L1], [H, H|L2]) :- duplicate(L1, L2).

/** duplicate the elements of a list a given number of times */
n_times_dupli(L1, N, L2) :- n_times_dupli(L1, N, L2, N).
/* base case */
n_times_dupli([], _, [], _).
n_times_dupli([_|L1], N, L2, 0) :- n_times_dupli(L1, N, L2, N).

n_times_dupli([H|L1], N, [H|L2], K) :- K > 0,
                K1 is K - 1, n_times_dupli([H|L1], N, L2, K1).

/* split a list into 2 parts, the length of the first part is given */
split_2(L, 0, [], L).
split_2([H|T], N, [H|L1], L2) :- N > 0, K is N-1, split_2(T, K, L1, L2).

/* remove a k'th element from a list */
remove_at(H, [H|T], 1, T).
remove_at(X, [H|T], N, [H|R]) :- N > 0, K is N - 1, remove_at(X, T, K, R).

/* insert an element into a list at given position */
insert_at(X, L, 0, [X|L]).
insert_at(X, [H|T], N, [H|L]) :- N > 0, K is N - 1, insert_at(X, T, K, L).

/* create a list containing all integers within a range */
range(Min, Max, [Min]) :- Min = Max.
range(Min, Max, [Min|L]) :- Min < Max, X is Min + 1, range(X, Max, L).
