# 有n个整数，使其前面各数顺序向后移m个位置，最后m个数变成最前面的m个数

import collections

m = int(input('移动位数：'))
a = [1, 23, 52, 2, 88, 12]
deq = collections.deque()
deq.extend(a)
deq.rotate(m)
print(a)
print(deq)
