# 位取反、位移动
# 取一个整数a从右端开始的4〜7位

a = int(input('输入一个数字: '))
b = 0                 # 0
b = ~b                # -1
print(bin(b))
b = b << 4            # -10000
b = ~b                # 1111
c = a >> 3
d = c & b
print('a:', bin(a))
print('b:', bin(b))
print('c:', bin(c))
print('d:', bin(d))
