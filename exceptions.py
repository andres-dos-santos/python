try:
  number = int("abc")
  print(number)
except ValueError:
  print("Não foi possível converter para número!")

try:
    x = int("10")
    y = 1 / 0
except ValueError:
    print("Erro de conversão!")
except ZeroDivisionError:
    print("Não pode dividir por zero!")

try:
  num = int("20")
except ValueError:
  print("Erro de conversão")
else:
  print("Conversão de certo: ", num)
finally:
  print("Fim da execução.")

def divide(x, y):
  if y == 0:
     raise ZeroDivisionError("Você tentou dividir por zero.")
  return x / y

print(divide(10, 2))
