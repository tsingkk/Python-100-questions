# 从键盘输入一个字符串，将小写字母全部转换成大写字母，然后输出到一个磁盘文件中保存
# 磁盘文件为同目录下 exa098.txt

filename = input('输入文件名:\n')
string = input('please input a string:\n')
string = string.upper()
fp = open(filename, "w")
fp.write(string)
fp.close()
