# 将一个整数分解质因数。例如：输入90,打印出90=2*3*3*5。

n = int(input("输入一个整数："))
print(n, '=', end=' ')
if n < 0:
    n /= -1
    print('-1 *', end=' ')
flag = 1
if n == 0:
    print('0')
    flag = 0
while flag:
    for i in range(2, int(n+1)):
        if n % i == 0:
            print('%d' % i, end=' ')
            flag = 0
            if n != i:
                flag = 1
                print('*', end=' ')
            n /= i
            break