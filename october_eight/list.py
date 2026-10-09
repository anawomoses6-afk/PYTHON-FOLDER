# number One
from random import randint

program = [randint(1, 50) for _ in range(10)]
print(program)


# number two
length = 0
for _ in numbers:
    length += 1
print(f"Length of the list: {length}")


# number three (0-indexed: 0, 2, 4, 6, 8)
sumof_even = 0
for index in range(0, length, 2):
    sumof_even += numbers[index]
print(f"Sum of elements at even positions: {sumof_even}")


# number four (0-indexed: 1, 3, 5, 7, 9, 11, 13, 15, 17, 19)
sumof_odd = 0
for index in range(1, length, 2):
    sumof_odd += numbers[index]
print(f"Sum of elements at odd positions: {sumof_odd}")



# number five (0-indexed: 2, 5, 8, 11, 14, 17, 20)
thirdproduct = 1
for index in range(2, length, 3):
    thirdproduct *= numbers[index]
print(f"elements at every third position: {thirdproduct}")



# number six (without sum() or len())
sum_of_total = 0
for star in numbers:
    sum_of_total += star

average = sum_of_total / length
print(f"Average of all the elements: {average:.2f}")




