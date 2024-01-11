x = eval(input(""))
y = eval(input(""))

# TODO

distance = ((x - 5) ** 2 + (y - 6) ** 2) ** 0.5

if distance <= 15:
    print("Inside")
else:
    print("Outside")
"""
Inside
Outside
"""

"""
請使用選擇敘述撰寫一程式
，讓使用者輸入一個點的平面座標x和y值
，判斷此點是否與點(5, 6)的距離小於或等於15
，如距離小於或等於15顯示【Inside】
，反之顯示【Outside】。
"""
