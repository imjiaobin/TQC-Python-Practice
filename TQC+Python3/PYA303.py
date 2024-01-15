# TODO

num = int(input(""))

if num < 100:
    for i in range(1, num + 1):
        for j in range(1, i + 1):
            print("{:>4}".format(i * j), end="")
        print("")

"""
請使用迴圈敘述撰寫一程式
，讓使用者輸入一個正整數（<100）
，然後以三角形的方式依序輸出此數的相乘結果。
提示：輸出欄寬為4，且需靠右對齊。
   1
   2   4
   3   6   9
   4   8  12  16
   5  10  15  20  25
"""
