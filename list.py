fruits = ["maça", "banana", "laranja"]
mixed = [10, "maça", True, 3.56]
numbers = [10, 20, 3, 56]

numbers.reverse()
print(numbers)
numbers.sort()
print(numbers)

print(fruits[0])
print(fruits[-2])

fruits[0] = "uva"
print(fruits)

fruits.append("morango")
print(fruits)

fruits.insert(1, "pera")
print(fruits)

fruits.remove("banana")
print(fruits)

print("pera" in fruits)
print("banana" in fruits)

print(len(numbers))
print(min(numbers))
print(max(numbers))
print(sum(numbers))

headquarters = [
  [1, 2, 3, 4],
  [9, 2, 13, 6],
  [10, 21, 0, 3],
]

print(headquarters[1][2])  # 13 (linha 1, coluna 2)