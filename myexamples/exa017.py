# 输入一行字符，分别统计出汉字、英文字母、空格、数字和其它字符的个数。

words = input('输入一行文字：')
zhnum = 0
ennum = 0
spanum = 0
numnum = 0
elnum = 0
for i in words:
    if u'\u4e00' <= i <= u'\u9fff':
        zhnum += 1
    elif i.isalpha():
        ennum += 1
    elif i.isdigit():
        numnum += 1
    elif i.isspace():
        spanum += 1
    else:
        elnum += 1
print('汉字%d个，字母%d个，数字%d个，空格%d个，其他符号%d个' % (zhnum, ennum, numnum, spanum, elnum))
