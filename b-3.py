a = int(input("行数を入力してください:"))
b = int(input("列数を入力してください:"))

for i in range(1, a+1):
    for j in range(1, b+1):
        print(i, "X", j, "=", i * j, end=" ❘ ")
    print()