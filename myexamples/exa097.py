# 从键盘输入一些字符，逐个把它们写到磁盘文件上，直到输入一个 # 为止
# 磁盘文件为同目录下 exa097.txt

if __name__ == '__main__':
    filename = input('输入文件名:\n')
    fp = open(filename, "w")
    ch = input('输入字符串:\n')
    while ch != '#':
        fp.write(ch)
        ch = input('输入字符串:\n')
    fp.close()
