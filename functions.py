# Aqui se o usuário não passar o nome, entra como "Visitante"
def welcome(city, name = "Visitante"):
  print(f"1: Olá {name}, você veio de {city}.")

welcome("Juiz de Fora")

def sum(x, y):
  return x + y
print("2: A soma é de: ", sum(1, 4.5))

# Ex.: 1

def even_or_odd(number):
  even = number % 2 == 0
  print("É par." if even else "É ímpar.")
