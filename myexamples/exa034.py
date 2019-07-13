# 练习函数调用。


def halloworld(n):
    print('Hallo World! ' * n)


def myname(names):
    print('%s is king of the world!' % names)


if __name__ == "__main__":
    n = int(input('请输入一个正整数：'))
    names = input('请输入你的名字：')
    halloworld(n)
    myname(names)
