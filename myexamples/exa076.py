# 编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n


def evennum(n):
    a = 0
    for i in range(2, n+1, 2):
        a += 1/i
    return a


def oddnum(n):
    a = 0
    for i in range(1, n+1, 2):
        a += 1/i
    return a


n = int(input("输入一个正整数："))
if n % 2 == 0:
    print('%.2f' % evennum(n))
else:
    print('%.2f' % oddnum(n))
