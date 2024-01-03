# TODO
x1 = eval(input())
y1 = eval(input())
x2 = eval(input())
y2 = eval(input())

dis = ((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) ** 0.5
print("( {} , {} )".format(x1, y1))
print("( {} , {} )".format(x2, y2))
print("Distance = {:.4f}".format(dis))
"""
Distance = _
請撰寫一程式，讓使用者輸入四個數字x1、y1、x2、y2，分別代表兩個點的座標(x1, y1)、(x2, y2)。計算並輸出這兩點的座標與其歐式距離。
兩座標的歐式距離，輸出到小數點後第4位
"""
