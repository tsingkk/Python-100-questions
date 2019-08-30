# 使用lambda来创建匿名函数。

nsquar = lambda a,b: a**b
x = float(input('x='))
y = float(input('y='))
print('x的y次方等于%.2f' % nsquar(x, y))