[
  "abfolge",
  [
    ["setzen", "sq", ["klasse_instanz", "Square", "sq", 3]],
    ["setzen", "ci", ["klasse_instanz", "Circle", "ci", 2]],
    ["setzen", "sq_density", ["shape_density", "sq", 5]],
    ["setzen", "ci_density", ["shape_density", "ci", 5]],
    ["setzen", "total_density", ["addieren", ["abrufen", "sq_density"], ["abrufen", "ci_density"]]],
    ["drucken", ["abrufen", "total_density"]]
  ]
]
