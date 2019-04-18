import time

for i in range(5):
    a = time.localtime()
    print(time.strftime('%Y-%m-%d %H:%M:%S',a))
    time.sleep(1)