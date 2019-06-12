import math

n = 0
for i in range(100, 201):
    k = 1
    for j in range(2, int(math.sqrt(i))+1):
        if i % j == 0:
            k = 0
            break
    if k:
        print('%d' % i)
        n += 1
print('共%d个素数' % n)
