# 输出一个随机数。
# 使用 random 模块。

import random
print(random.randint(1,101))        # 产生 1 到 100 的一个整数型随机数  
print(random.random())              # 产生 0 到 1 之间的随机浮点数
print(random.uniform(1.1,5.4))      # 产生  1.1 到 5.4 之间的随机浮点数，区间可以不是整数
print(random.choice('python'))      # 从序列中随机选取一个元素
print(random.randrange(0,101,2))    # 生成从1到100的间隔为2的随机整数