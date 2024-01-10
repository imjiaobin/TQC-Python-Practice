# TODO

y = int(input(""))

if y % 400 == 0:
    print(f"{y} is a leap year.")

elif y % 4 != 0 or y % 100 == 0:
    print(f"{y} is not a leap year.")

else:
    print(f"{y} is a leap year.")

"""
請使用選擇敘述撰寫一程式
，讓使用者輸入一個西元年份
，然後判斷它是否為閏年（leap year）或平年。
其判斷規則為：每四年一閏，每百年不閏，但每四百年也一閏。
"""
