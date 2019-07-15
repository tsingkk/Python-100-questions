# 对10个数进行排序(不用列表的排序方法)。

a = [12, 24, 33, 1, 54, 55, 23, 11, 12, 100]
for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[i] >= a[j]:
            a[i], a[j] = a[j], a[i]
print(a)
