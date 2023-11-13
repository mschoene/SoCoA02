["abfolge",
  ["setzen", "a", 0 ],
  ["setzen", "li", ["liste" , 0, 1,2,3,4 ]],
  ["setzen", "li_sq", ["liste" , 0, 1,2,3,4]],
  ["setzen", "li_double", ["liste" , 0, 1,2,3,4]],

  ["waehrend",["kleiner_als", ["abrufen", "a"] , 5], 
    ["abfolge", 
    ["drucken", "iteration nr. ", ["abrufen", "a"]], 
    ["setzen_listenObj", "li_sq", ["abrufen", "a"], ["hochstellen", ["abrufen", "a"], 2 ] ],
    ["setzen_listenObj", "li_double", ["abrufen", "a"], ["multiplizieren", ["abrufen", "a"], 2 ] ],
    ["drucken", "new list value at index is squared ", ["abrufen", "a"] , " = ", ["abrufen_listenObj", "li_sq",  ["abrufen", "a"]]], 
    ["drucken", "new list value at index is doubled ", ["abrufen", "a"] , " = ", ["abrufen_listenObj", "li_double",  ["abrufen", "a"]]], 
    ["setzen", "a", ["addieren", ["abrufen", "a"] , 1] ]
    ] 
  ],
  ["setzen", "dict_sq", ["woerterbuch",   ["abrufen", "li"],   ["abrufen", "li_sq"] ] ],
  ["setzen", "dict_double", ["woerterbuch",   ["abrufen", "li"],   ["abrufen", "li_double"] ] ],

  ["setzen_schluessel_wert", "dict_double", 4, 42 ],
  ["setzen_schluessel_wert", "dict_double", 3, ["dividieren", 1, ["abrufen_schluessel", "dict_double", 4 ] ]],
  ["drucken", "the answer is = ",  ["abrufen_schluessel", "dict_double", 4 ]] ,
  ["drucken", "1/answer is = " , ["abrufen_schluessel", "dict_double", 3 ]] ,

  ["setzen", "wombocombo", ["woerterbuch_vereinigung", ["abrufen", "dict_sq"], ["abrufen", "dict_double"]]],
  ["drucken", "combined dictionary = ", ["abrufen", "wombocombo"]]
]