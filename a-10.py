# ここにコードを記述
import random


def dice():
    result = random.randint(1, 6)
    return result


print(dice())  # 1から6の整数をランダムに出力する
