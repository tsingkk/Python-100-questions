# 给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。

n = input('输入一个不多于5位的正整数：')
print('%d位数' % len(n))
n = list(n)
n.reverse()
print(n)
for i in n:
    print(i)
