year = int(input("年："))
month = int(input("月："))
day = int(input("日："))
daysofmonths = [0, 31, 28, 31, 30, 31, 30, 31, 31,
                30, 31, 30]
sumdays = 0
if (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)):
    daysofmonths[2] += 1
for i in range(month):
    sumdays += daysofmonths[i]
print("这一天是今年的第%d天" % (sumdays+day))
