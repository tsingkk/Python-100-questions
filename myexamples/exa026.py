# 利用递归方法求阶乘5!。

def jiecheng(n):
    if n != 1:
        return (n * jiecheng(n - 1))
    else:
        return 1

print(jiecheng(5))