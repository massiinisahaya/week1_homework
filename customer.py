class Customer:
    # 各問のコードが期待通り動作するように実装
    def full_name(self):
        


ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
tom = Customer(first_name="Tom", family_name="Ford", age= 57)
ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=75)

# 以降で各問のコードを追加していく
print(ken.full_name())  # "Ken Tanaka" という値を出力
print(tom.full_name())  # "Tom Ford" という値を出力
