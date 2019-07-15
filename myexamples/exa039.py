# 有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。

a = [10, 21, 33, 53, 99, 211]
n = int(input('输入一个整数：'))
a.append(n)
for i in range(len(a)-1, 0, -1):
    if a[i] < a[i-1]:
        a[i], a[i-1] = a[i-1], a[i]
print(a)
