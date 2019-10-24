# 写一个函数，求一个字符串的长度，在main函数中输入字符串，并输出其长度。


def chang(a):
    return len(a)


if __name__ == "__main__":
    a = input("输入一个字符串：")
    print("字符串长度为%d" % chang(a))
