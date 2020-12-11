# gewoone list
from typing import List

my_data = ["data1", "data2", 0.1, 42]
print(my_data)

# list aanmaken met een list comprehension
numbers = [n for n in range(1, 1001) if n % 2 == 0]
print(numbers)

# list met een while statement en append function
numbers_1 = []
n = 2
while n < 1002:
    numbers_1.append(n)
    n = n+2
print(numbers_1)

# list met range en een step
numbers_2 = list(range(2, 1001, 2))
print(numbers_2)
