# TODO
# TQC+ 程式語言Python 310 迴圈公式計算
n = int(input())
tot = 0
for i in range(2, n + 1):
    tot = tot + 1 / ((i - 1) ** 0.5 + (i**0.5))
print("{:.4f}".format(tot))
