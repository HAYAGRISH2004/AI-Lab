has_fur(cat).
has_fur(dog).
lays_eggs(duck).
gives_milk(cat).
barks(dog).
quacks(duck).


mammal(X) :- has_fur(X), gives_milk(X).
bird(X) :- lays_eggs(X).
mammal(X) :- barks(X).


is_mammal(X) :- mammal(X).
is_bird(X) :- bird(X).
