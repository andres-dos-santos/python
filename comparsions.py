y = 10
x = 5

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

print(3 < x < 20)

name1 = "Andres"
name2 = "Bruno"

print(name1 == name2) # False
print(name1 < name2) # True (A vem antes de B)

a = [1,2,3]
b = a
c = [1,2,3]

print(a == c) # True, valores iguais
print(a is c) # False, objetos diferentes
print(a is b) # True, mesmos objetos

age = 18

if age >= 18:
  print("Maior de idade.")
else:
  print("Menor de idade.")