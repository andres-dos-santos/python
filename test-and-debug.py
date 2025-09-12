import pdb

def sum(x, y):
  result = x + y
  print("Dentro da função, resultado = ", result)
  return result
sum(10, 5)

def sum(x, y):
  # pdb.set_trace()  # código para por causa do debug
  result = x + y
  print("Dentro da função, resultado = ", result)
  return result

sum(10, 5)

# a vantagem aqui é que pode ser testado várias situações de forma rápida
def sum(a, b):
    return a + b

assert sum(2, 3) == 5
assert sum(-1, 1) == 0
assert sum(0, 0) == 0

print("Todos os testes passaram!")

