# Escopo é a região do código onde uma variável pode ser acessada

name = "Andres" # variável global

def greeting():
  message = "Welcome!"
  print(f"{message}, {name}")

greeting()

print(name) # aqui funciona porque tem o escopo global
#print(message) #ERROR: porque message está dentro do escopo da função

x = 5
def sum():
  x = 10
  print("Dentro do escopo de 'sum': ", x) # soma apenas o que está dentro do escopo

sum()
print("Fora do escopo de 'sum': ", x)

count = 10
def increment():
  global count
  count += 1
increment()
increment()
print("Usando o escopo global dentro da função 'increment': ", count) # 12 porque eu usei o 'global' para usar a variável global dentro do escopo correto

def extern():
  x = "Escopo externo"

  def intern():
    nonlocal x
    x = "modificação pela interna"
    print("Dentro da interna: ", x)

  intern()
  print("Dentro da externa: ", x)

extern()

# ⚠️ CUIDADO COM O `UnboundLocalError`: O erro aparece quando você tenta usar uma variável local antes de ela ter um valor atribuído dentro do escopo da função.