% Facts and rules representing the graph (example graph)

edge(a, b, 3).
edge(a, c, 2).
edge(b, d, 4).
edge(b, e, 5).
edge(c, f, 3).
edge(c, g, 4).


goal(g).


bfs(Start, Goal) :- bfs([(0, Start, [])], Goal, []).

bfs([(Cost, Node, Path) | _], Goal, _):-
    Goal = Node,
    reverse(Path, Solution),
    write('Solution Path: '), write(Solution).

bfs([(Cost, Node, Path) | Rest], Goal, Visited) :-
    Goal \= Node,
    \+ member(Node, Visited),
    findall((NewCost, NewNode, [Node | Path]),
        (edge(Node, NewNode, StepCost), NewCost is Cost + StepCost),
        Children),
    append(Children, Rest, NewQueue),
    sort(NewQueue, SortedQueue),
    bfs(SortedQueue, Goal, [Node | Visited]).
