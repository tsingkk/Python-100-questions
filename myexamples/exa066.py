# 输入5个整数，按大小顺序输出

a = []
for i in range(5):
    a.append(int(input('输入一个整数：')))
print(sorted(a))
