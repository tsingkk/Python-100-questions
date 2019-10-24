# 输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组。

a = [1, 23, 52, 2, 88, 12]
a[-1], a[a.index(min(a))] = a[a.index(min(a))], a[-1]
print(a)
b = a[0]
c = a.index(max(a))
a[0] = a[c]
a[c] = b
print(a)
