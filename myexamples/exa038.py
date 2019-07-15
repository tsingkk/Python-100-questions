# 求一个3*3矩阵主对角线元素之和。

a = [
    [2, 3, 9],
    [6, 10, 26],
    [5, 13, 14]
]
sum = 0
for i in range(len(a)):
    sum += a[i][i]
print(sum)
