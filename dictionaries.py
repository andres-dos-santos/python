people = {
  "name": "Andres dos Santos",
  "age": 24,
  "city": "Juiz de Fora"
}

print(people["age"])
print(people.get("height", "height não informado!"))

people["occupation"] = "Mid frontend"
print(people)

del people["occupation"]
# people.clear() # limpa todo o dicionário

# itera apenas a chave 
for key in people:
  print(key)

# itera apenas os valores
for value in people.values():
  print(value)

# itera chave e valor
for key, value in people.items():
    print(key, "=>", value)

