side1 = eval(input())
side2 = eval(input())
side3 = eval(input())

# TODO

com1 = side1 + side2
com2 = side1 + side3
com3 = side2 + side3

if com1 > side3 and com2 > side2 and com3 > side1:
    print(side1 + side2 + side3)
else:
    print("Invalid")
"""
Invalid
"""

"""
請使用選擇敘述撰寫一程式
，讓使用者輸入三個邊長
，檢查這三個邊長是否可以組成一個三角形。
若可以，則輸出該三角形之周長
；否則顯示【Invalid】。

提示：檢查方法 = 任意兩個邊長之總和大於第三邊長。
"""
