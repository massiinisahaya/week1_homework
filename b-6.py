import random

side_of_dice = input("サイコロの面の数は?: ")
number_of_roll = input("何回振りますか?: ")

n = int(side_of_dice)
m = int(number_of_roll)

numbers = []
for number in range(m):
    dice_number = random.randrange(1, n)
    numbers.append(dice_number)

print(numbers)
