# 打印出如下图案（菱形）:
# &nbsp;&nbsp;&nbsp;&nbsp;\*
# &nbsp;&nbsp;&nbsp;\*\*\*
# &nbsp;&nbsp;\*\*\*\*\*
# &nbsp;\*\*\*\*\*\*\*
# &nbsp;&nbsp;\*\*\*\*\*
# &nbsp;&nbsp;&nbsp;\*\*\*
# &nbsp;&nbsp;&nbsp;&nbsp;\*


def draw(n):
    a = '*' * (2 * (4 - n) + 1)
    print(a.center(9, ' '))
    if n != 1:
        draw(n - 1)
        print(a.center(9, ' '))
draw(4)
