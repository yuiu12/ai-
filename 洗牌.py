'''
四种花色每种各十三张牌，可以使用排列组合的方式变成一副牌
根据随机选择的人作为地主并修改他的值，可以使用eval函数
随机分配需要使用random模块
'''
import random 
suits = ['♥', '♠', '♣', '♦']
cardstr = ['J', 'Q', 'K', 'A']
cardnum = [str(i) for i in range(2, 11)]
cardking = ['大王', '小王']

card = [] 
for suit in suits:
    for num in cardnum:
        card.append(suit + num) 
    for str in cardstr:
        card.append(suit + str) 
card = card + cardking 
#打乱顺序
random.shuffle(card)
#不重复元素
地主牌 = random.sample(card,6)
x = random.choice(['A','B','C','D'])
for i in 地主牌:
    card.remove(i) 
A = [] 
B = [] 
C = [] 
D = [] 
for i in range(len(card)):
    if i % 4 == 0:
        A.append(card[i]) 
    if i % 4 == 1:
        B.append(card[i]) 
    if i % 4 == 2:
        C.append(card[i]) 
    if i % 4 == 3:
        D.append(card[i]) 
#字符串的表达式，返回表达式的值

eval(x).extend(地主牌)
print(f'地主牌是{地主牌}，地主是{x}')
print(f'A:{A}')
print(f'B:{B}')
print(f'C:{C}')
print(f'D:{D}')

