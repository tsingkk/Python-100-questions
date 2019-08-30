# 两个变量值用函数互换。

def exnum(a, b):
    return (b, a)
a = 1
b = 2
a,b = exnum(a, b)
print(a,b)