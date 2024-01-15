# TODO

times = int(input(""))

for i in range(times):
    num = input("")
    total = 0
    for j in range(len(num)):
        total = total + int(num[j])
    print("Sum of all digits of {} is {}".format(num, total))

"""
Sum of all digits of _ is _
"""
"""
請使用迴圈敘述撰寫一程式
，要求使用者輸入一個數字
，此數字代表後面測試資料的數量。
每一筆測試資料是一個正整數（由使用者輸入）
，將此正整數的每位數全部加總起來。
"""
