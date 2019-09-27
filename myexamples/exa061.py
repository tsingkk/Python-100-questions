# 打印出杨辉三角形前十行


def yanghui(rows):
    a = [[1]]
    for i in range(rows):
        b = list(map((lambda x, y: x+y), a[-1]+[0], [0]+a[-1]))
        a.append(b)
    return a[:rows]


n = int(input('杨辉三角行数：'))
for i in yanghui(n):
    print(i)
