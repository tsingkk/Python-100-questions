# 两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。
# 已抽签决定比赛名单。有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，
# 请编程序找出三队赛手的名单。

a = set(['y', 'z'])
b = set(['x', 'y', 'z'])
c = set('y')
for i in a:
    for j in b:
        for k in c:
            if len(set([i, j, k])) == 3:
                print('a vs %s, b vs %s, c vs %s' % (i, j, k))
