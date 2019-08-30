# 求输入数字的平方，如果平方运算后小于 50 则退出。

while True:
    a = int(input('输入一个数：'))
    print('%d的平方为%d' % (a, a**2))
    if a**2 < 50:
        print('平方小于50，程序推出')
        break
