["abfolge",
["klasse", ["setzen", "Shape", ["woerterbuch", ["liste", "_classname", "_parent", "density"], ["liste", "Shape", "None", ["funktion", ["thing", "weight"], ["dividieren", ["abrufen", "weight"], ["klassen_aufrufen", ["abrufen", "thing"], "area", ["abrufen", "thing"]]]]]]]],

["klasse", ["setzen", "Square", ["woerterbuch", ["liste", "_classname", "_parent", "area"], ["liste", "Square", ["abrufen", "Shape"], ["funktion", ["thing"], ["hochstellen", ["abrufen_schluessel", "thing", "side"], 2]]]]]],
["klassen_instanz", ["setzen", "sq", ["woerterbuch", ["liste", "name", "side", "_class"], ["liste", "sq", "3", ["abrufen", "Square"]]]]],

["klasse", ["setzen", "Circle", ["woerterbuch", ["liste", "_classname", "_parent", "area"], ["liste", "Circle", ["abrufen", "Shape"], ["funktion", ["thing"], ["multiplizieren", ["hochstellen", ["abrufen_schluessel", "thing", "radius"], 2], 3.14]]]]]],
["klassen_instanz", ["setzen", "ci", ["woerterbuch", ["liste", "name", "radius", "_class"], ["liste", "ci", "2", ["abrufen", "Circle"]]]]],


["drucken", ["addieren", ["klassen_aufrufen", ["abrufen", "sq"], "density", ["abrufen", "sq"], 5], ["klassen_aufrufen", ["abrufen", "ci"], "density", ["abrufen", "ci"], 5]]]
]
