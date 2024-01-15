# TODO

amount = eval(input(""))
rate = eval(input(""))
month = eval(input(""))
print("{} \t  {}".format("Month", "Amount"))

total = amount
for i in range(1, month + 1):
    total = total + total * rate / 1200
    print("%3d \t %.2f" % (i, total))

"""
請使用迴圈敘述撰寫一程式
，提示使用者輸入金額（如10,000）、年收益率（如5.75）
，以及經過的月份數（如5），接著顯示每個月的存款總額。
"""
