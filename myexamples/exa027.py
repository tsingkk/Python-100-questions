# 利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。

def func1(n):
    if len(n) != 1:
        func1(n[1:])
    print(n[0])


func1(input('输入一串字符：'))