fruits = ["maça", "banana", "laranja"]

for fruit in fruits:
  print(fruit)

for i in range(5):
  print(i)

# range(início, fim, passo)
for i in range(2, 10, 2):
  print(i)

count = 0

while count < 5:
  print("Count = ", count)
  count += 1

for i in range(10):
  if i == 5:
    break
  print(i)

name = "Andres"
for letter in name:
  print(letter)