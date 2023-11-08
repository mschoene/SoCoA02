["abfolge",
  ["setzen", "double",
    ["funktion", ["num"],
      ["addieren", ["abrufen", "num"], ["abrufen", "num"]]
    ]
  ],
  ["setzen", "a", 1],
  ["aufrufen", "double", ["abrufen", "a"]],
  ["dividieren", 3, 2],
  ["waehrend", ["abrufen", "a"]  , ["abfolge", ["drucken", ["abrufen", "a"]], ["setzen", "a", ["addieren", ["abrufen", "a"], 1 ]]   ]]

]