import math

numbers = input("データを入力してください(スペース区切り) \033[31m > \033[0m")
cleaned_numbers = numbers.replace(",", " ")
print(cleaned_numbers)

numbers_link = [int(numbers) for numbers in cleaned_numbers.split()]

total = 0
for number in numbers_link:
    total += number

print(f"合計値: {total}")

max_number = numbers_link[0]  # 初期値としてリストの最初の数値を設定
for number in numbers_link:
    if number > max_number:
        max_number = number

print(f"最大値: {max_number}")

min_number = numbers_link[0]

for number in numbers_link:
    if number < min_number:
        min_number = number

print(f"最小値: {min_number}")

total = 0
for number in numbers_link:
    total += number

average_number = math.floor(total / len(numbers_link))

print(f"平均値: {average_number}")
