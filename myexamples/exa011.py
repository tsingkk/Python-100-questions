month = int(input("输入繁殖几个月："))
month1 = 1
month2 = 0
month3 = 0
if month == 1:
    print(
        "满1月兔%d对\n满2月兔%d对\n满3月兔%d对\n兔子总共%d对" %
        (month1, month2, month3, month1+month2+month3)
        )
else:
    for i in range(month-1):
        month1, month2, month3 = month3, month1, month2+month3
    print(
        "满1月兔%d对\n满2月兔%d对\n满3月兔%d对\n兔子总共%d对" %
        (month1, month2, month3, month1+month2+month3)
        )
