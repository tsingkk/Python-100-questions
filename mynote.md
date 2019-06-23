- 类似print("这一天是今年的第%d天" % (sumdays+day))这种行类有计算表达式的，应将表达式用（）括起
- 如果 list 是一个空的，没有一个元素的列表，使用 list[0]，会出现**IndexError: list index out of range**
- **copy.copy** 浅拷贝 只拷贝父对象，不会拷贝对象的内部的子对象，效果同[:]。
- **copy.deepcopy** 深拷贝 拷贝对象及其子对象
- **print('%d*%d=%d' % (j,i,j*i),end=' ')**，此类格式化输出多个变量，%后为元组
- **with open() as foo**，用foo.readlines()后，再用foo.read()无法读取，可能原因：foo.readlines()运行完句柄就自动关闭了？或者是foo.readlines()已经读取到文件最后，句柄之后无内容了，所以再foo.readlines()无内容。
- **open()**中最好加encoding参数，否则windows系统可能识别不出文件编码
- **r'e:\documents\'**，windows下的路径名采用此种格式，避免**转义字符（反斜杠）**导致出错
- **PEP8's E128: continuation line under-indented for visual indent**，避免出现此种警告，可使用以下括号断行写法：
    ```
    print(
        "aaaaa",
        "vvvvv",
        "ccccc"
    )
- **with open() as foo**，用foo.readlines()后，再用foo.read()无法读取，可能原因：foo.readlines()运行完句柄就自动关闭了？或者是foo.readlines()已经读取到文件最后，句柄之后无内容了，所以再foo.readlines()无内容。
- **open()**中最好加encoding参数，否则windows系统可能识别不出文件编码
- **r'e:\documents\'**，windows下的路径名采用此种格式，避免**转义字符（反斜杠）**导致出错
- **浮点数取整**，int():向下取整，round()：四舍五入，ceil()：向上取整
- **中文汉字的unicode编码**范围是u'\u4e00'~u'\u9fff'
- **set()函数**，最多只能有一个参数，为可迭代对象，如列表、字符串等
