resultado_array = resultado.split("\n")

simple_database = []

for linha in resultado_array:

  if "open" in linha and linha not in simple_database:
    simple_database.append(linha)

for row in simple_database:
  print(row)
