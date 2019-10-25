# 求1亿以内0—7所能组成的奇数个数。

sum = 4
for i in range(2, 9):
    s = 4 * 7 * 8 ** (i-2)
    print(s)
    sum += s
print('sum=%d' % sum)
