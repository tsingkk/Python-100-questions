# 一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。

n = input('输入一个5位数：')
if n[0] == n[4] and n[1] == n[3]:
    print('这是一个回文数。')
else:
    print('这不是一个回文数。')