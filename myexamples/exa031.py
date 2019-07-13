# 请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。

weekname = {
    'm': 'Monday',
    'w': 'Wednesday',
    'f': 'Friday',
    't': {
         'u': 'Tuesday',
         'h': 'Thursday '
    },
    's': {
        'a': 'Saturday',
        'u': 'Sunday'
    }
}
i = 1
a = weekname
while True:
    n = input('输入星期几的第%d个字母：' % i)
    if isinstance(a[n], str):
        print(a[n])
        break
    else:
        i += 1
        a = a[n]
