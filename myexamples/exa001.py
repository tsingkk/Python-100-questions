t = 0
for a in range(1, 5):
    for b in range(1, 5):
        for c in range(1, 5):
            if (a != b) and (b != c) and (c != a):
                print(a, b, c)
                t += 1
print("符合条件的数字个数：", t)