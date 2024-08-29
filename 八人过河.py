'''
现在有8个人分别为：1个父亲，带着他的2个儿子。1个母亲，带着她的2个女儿；1个警察，带着1个犯人； 开始时，8个人都是在河的左岸。现在需要过河，过河时需要注意下面5条说明：
1，只有警察、父亲和母亲可以划船；
2，警察如果离开犯人，犯人就会伤害其他人；
3，母亲不在时，这个父亲会伤害她的女儿。
4，父亲不在时，这个母亲也会伤害他的儿子；
5，船上一次最多只能坐两个人。
试用python求出过河方案。
'''
left,ship,right,ship2 = ['警察','犯人','父亲','儿子','儿子','母亲','女儿','女儿'],[],[],[]
i = j = t = 0 
def rules(left1,right1,ship1):
    x = [left1,right1,ship1] 
    for i in x:
        if ('父亲' not in i) and ('母亲' in i)  and ('儿子' in i):
            assert False 
        if ('母亲' not in i) and ('父亲' in i) and ('女儿' in i) :
            assert False
        if ('警察' not in i) and ('犯人' in i) and (len(i)!=1):
            assert False
        if (i==ship1):
            if '父亲' not in i and '母亲' not in i and '警察' not in i:
                assert False
def actions_1(ship1,right1,left1):
    global ship,right,left,i,j,ship2 
    while True:
        left1 = left[:] 
        ship1 = ship[:] 
        right1 = right[:] 
        ship1.append(left1.pop(i))
        ship1.append(left1.pop(j))
        for k in ship1:
            right1.append(k)
        try:
            rules(left1,right1,ship1)
            if sorted(ship1)==sorted(ship2):
                assert False
            break
        except:
            j=j+1
            if j>len(left1):
                i=i+1
                j=i
            if i == len(left1)+1:
                break
    ship2=ship1
    ship=[]
    right=right1
    left=left1
    i=j=0
def actions_2(ship1,right1,left1):
    global ship,right,left,i,j,t,ship2
    while True:
            left1=left[:]
            ship1=ship[:]
            right1=right[:]
            ship1.append(right1.pop(t))
            for k in ship1:
                left1.append(k)
            try:
                rules(left1,right1,ship1)
                break
            except:
                t=t+1
                if t == len(right1)+1:
                    left1=left[:]
                    ship1=ship[:]
                    right1=right[:]
                    break
    if ship1==[]:
        while True:
            left1=left[:]
            ship1=ship[:]
            right1=right[:]
            ship1.append(right1.pop(i))
            ship1.append(right1.pop(j))
            for k in ship1:
                left1.append(k)
            try:
                rules(left1,right1,ship1)
                break
            except:
                j=j+1
                if j>len(right1):
                    i=i+1
                    j=i
                if i == len(right1)+1:
                    break
    ship2=ship1
    ship=[]
    right=right1
    left=left1
    i=j=t=0
while True:
    actions_1(ship,right,left)
    print(f'{ship2}从左往右')
    print(f'此时左边剩下{left}，右边剩下{right}')
    actions_2(ship,right,left)
    print(f'{ship2}从右往左')
    print(f'此时左边剩下{left}，右边剩下{right}')
    if len(left)==2:
        actions_1(ship,right,left)
        print(f'{ship2}从左往右')
        print(f'此时左边剩下{left}，右边剩下{right}')
        break