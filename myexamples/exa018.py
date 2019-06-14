# 求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。

num = input('输入一个数字：')
n = int(input('输入相加次数：'))
sum = 0
for i in range(n):
    sum += int(num)
    if i == (n - 1):
        print('%s =' % num, end=' ')
    else:
        print('%s +' % num, end=' ')
    num += num[0]
print(sum)
