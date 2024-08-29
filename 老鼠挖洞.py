'''
九章算术》的“盈不足篇”里有一个很有意思的老鼠打洞问题。原文这么说的：
今有垣厚十尺，两鼠对穿。大鼠日一尺，小鼠亦一尺。大鼠日自倍，小鼠日自半。问：何日相逢？各穿几何？
这道题的意思就是说，有一堵十尺厚的墙，两只老鼠从两边向中间打洞。大老鼠第一天打一尺，小老鼠也是一尺。
大老鼠每天的打洞进度是前一天的一倍，小老鼠每天的进度是前一天的一半。问它们几天可以相逢，相逢时各打了多少。
'''
all_big = all_small = big_mouse = small_mouse = 1 
x,day = 10,0 
while True:
    #求出总距离减去两只老鼠一起挖洞的距离剩余的距离并重新赋值给x
    x -= (big_mouse + small_mouse) 
    big_mouse *= 2 
    small_mouse /= 2 
    day += 1 
    if x <= 0:
        print(day) 
        break 
    all_big += big_mouse 
    all_small += small_mouse 
x = (10 - all_big - all_small) 
all_big += x * big_mouse / (big_mouse + small_mouse) 
all_small += x * small_mouse / (big_mouse + small_mouse) 
print(f'大老鼠挖了{all_big}尺，小老鼠挖了{all_small}尺')