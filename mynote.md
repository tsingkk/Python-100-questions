- 类似 print("这一天是今年的第%d 天" % (sumdays+day)) 这种行类有计算表达式的，应将表达式用（）括起
- 如果 list 是一个空的，没有一个元素的列表，使用 list[0]，会出现** IndexError: list index out of range**
- **copy.copy** 浅拷贝 只拷贝父对象，不会拷贝对象的内部的子对象，效果同 [:]。
- **copy.deepcopy** 深拷贝 拷贝对象及其子对象
- **print('%d*%d=%d' % (j,i,j*i),end=' ')**，此类格式化输出多个变量，%后为元组
- **with open() as foo**，用 foo.readlines() 后，再用 foo.read() 无法读取，可能原因：foo.readlines() 运行完句柄就自动关闭了？或者是 foo.readlines() 已经读取到文件最后，句柄之后无内容了，所以再 foo.readlines() 无内容。
- **open() **中最好加 encoding 参数，否则 windows 系统可能识别不出文件编码
- **r'e:\documents\'**，windows 下的路径名采用此种格式，避免**转义字符（反斜杠）**导致出错
- **PEP8's E128: continuation line under-indented for visual indent**，避免出现此种警告，可使用以下括号断行写法：
    ```
    print(
        "aaaaa",
        "vvvvv",
        "ccccc"
    )
- **with open() as foo**，用 foo.readlines() 后，再用 foo.read() 无法读取，可能原因：foo.readlines() 运行完句柄就自动关闭了？或者是 foo.readlines() 已经读取到文件最后，句柄之后无内容了，所以再 foo.readlines() 无内容。
- **open() **中最好加 encoding 参数，否则 windows 系统可能识别不出文件编码
- **r'e:\documents\'**，windows 下的路径名采用此种格式，避免**转义字符（反斜杠）**导致出错
- **浮点数取整**，int(): 向下取整，round()：四舍五入，ceil()：向上取整
- **中文汉字的 unicode 编码**范围是 u'\u4e00'~u'\u9fff'
- **set() 函数**，最多只能有一个参数，为可迭代对象，如列表、字符串等
- **逆序**：
    - `list.reverse()`无返回值，将 list 逆序，就地改变，所以`list = list.reverse()`此种写法会返回错误。
    - `reversed(seq)`返回将 seq 逆转后的迭代器，seq 为要转换的序列，可以是 tuple, string, list 或 range。
    - `print(seq[::-1])`可以将 seq 逆序打印，但不改变 seq 内部元素顺序。
- **list(seq).reverse()**, 此种写法返回空值。只能先`n = list(seq)`，再`n.reverse()`。
- **'\033 [显示方式；前景色；背景色 m' + 打印内容 + '\033[0m'**，用于终端中输出彩色字体。
- **range（起点，终点，步长）**，默认起点为 0，默认步长为 1，如果生成 3 2 1 这种从大到小的数组，必须写明步长。
- **git commit -m "xxx"**，提交的更新说明 xxx，必须用双引号括起来，单引号 git 不认。
- **按位运算符**，是将数转换为二进制（位数不够用 0 补位），然后对每个数位进行运算。
    - **按位异或 ^**：对位相加，但是不进位，即 1^1=0。
- **Tkinter 的 C.create_oval ( x0, y0, x1, y1, option, ... )**, 其中（x0, y0），（x1, y1）为所画圆外切四边形对角线两端座标。
- **数列排序的方法**：
    1. 利用循环冒泡排序
    2. sorted.() 函数
- **双向队列**，利用`collections.deque`创建和操作双向队列，将数组转化为双向队列，实现把右边元素放到左边操作。
- **eval () 函数**，用来执行一个字符串表达式，并返回表达式的值。如下示例：
    ```
    >>>x = 7
    >>> eval( '3 * x' )
    21
    >>> eval('pow(2,2)')
    4
    >>> eval('2 + 2')
    4
    >>> n=81
    >>> eval("n + 4")
    85
    ```
- **str.join(sequence)**，该字符串方法，以 str 连接序列 sequence 中的元素。
