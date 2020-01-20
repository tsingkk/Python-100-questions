# 有两个磁盘文件A和B,各存放一行字母,要求把这两个文件中的信息合并(按字母顺序排列), 输出到一个新文件C中
# 文件A：exa099a.txt
# 文件B：exa099b.txt
# 文件C：exa099c.txt

fp = open("f:\\documents\\projects\\H12练手python100题\\myexamples\\exa099a.txt")
a = fp.read()
fp.close()

fp = open('f:\\documents\\projects\\H12练手python100题\\myexamples\\exa099b.txt')
b = fp.read()
fp.close()

fp = open('f:\\documents\\projects\\H12练手python100题\\myexamples\\exa099c.txt',
          'w')
c = list(a + b)
print(c)
c.sort()
s = ''
s = s.join(c)
fp.write(s)
fp.close()
