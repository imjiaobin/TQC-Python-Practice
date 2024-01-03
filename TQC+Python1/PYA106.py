x = eval(input())  # min
y = eval(input())  # sec
z = eval(input())  # km

# TODO
# speed = (z / 1.6) / ((x * 60 + y) / 3600)
speed = (z / 1.6) / ((x + y / 60) / 60)
print("Speed = %.1f" % speed)
"""
Speed = _

假設一賽跑選手在x分y秒的時間跑完z公里
，請撰寫一程式
，輸入x、y、z數值
，最後顯示此選手每小時的平均英哩速度（1英哩等於1.6公里）。
"""
