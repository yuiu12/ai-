'''
两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定比赛名单。有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比。请编程序找出三队赛手的名单。

观察题意易知，c不与x和z比，那么c与y比，a不与x比，也不与y比，则a与z比，那么最后的b与x比，编写程序时也只需将三者一一对应即可
'''
乙队 = 'xyz'
for a in 乙队:
    for b in 乙队:
        for c in 乙队:
            if a != 'x' and c != 'x' and c != 'z' and a != b != c != a:
                print(f'a的对手是{a}，b的对手是{b}，c的对手是{c}')