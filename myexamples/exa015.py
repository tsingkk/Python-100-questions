# 利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。

n = float(input('输入考试分数：'))
if n >= 90:
    level = 'A'
elif 60 <= n < 89:
    level = 'B'
else:
    level = 'C'
print('成绩为%s' % level)