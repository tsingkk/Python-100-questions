# 输入一个奇数，然后判断最少几个 9 组成的数除以该数的结果为整数。
# 例如999999 / 13 = 76923。测试程序最好用 13，其他数可能会花很长时间运行程序。

a = int(input("输入一个奇数："))
x = 9
while x % a != 0:
    x = x * 10 + 9
print("%d / %d = %d" % (x, a, x/a))
