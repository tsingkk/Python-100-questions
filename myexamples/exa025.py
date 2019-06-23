# 求1+2!+3!+...+20!的和。


def jiecheng(n):
    if n != 1:
        return n * jiecheng(n-1)
    else:
        return 1


sum = 0
for i in range(1, 21):
    sum += jiecheng(i)
print(sum)
