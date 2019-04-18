n = int(input("输入数列长度："))

def fib(i):
    if i in (1, 2):
        thenumber = 1
    else:
        thenumber = fib(i-1) + fib(i-2)
    return thenumber

for i in range(n):
    print(fib(i+1))
