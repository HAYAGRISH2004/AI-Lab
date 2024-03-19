is_wet(rain).
is_cold(snow).
is_windy(wind).


weather(bad) :- is_wet(rain).
weather(bad) :- is_cold(snow).
weather(bad) :- is_windy(wind).


diagnose_weather(Condition) :-
    weather(Condition),
    write('The weather is '), write(Condition), nl.

