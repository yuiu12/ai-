'''
为便于确定五星之位置，先将旗面对分为四个相等的长方形，将左上方之长方形上下划为十等分，左右划为十五等分。
大五角星的中心点，在该长方形上五下五、左五右十之处。其画法为：以此点为圆心，以三等分为半径作一圆。在此圆周上，定出五个等距离的点，其一点须位于圆之正上方。然后将此五点中各相隔的两点相联，使各成一直线。此五直线所构成之外轮廓线，即为所需之大五角星。五角星之一个角尖正向
四颗小五角星的中心点，第一点在该长方形上二下八、左十右五之处，第二点在上四下六、左十二右三之处，第三点在上七下三、左十二右三之处，第四点在上九下一、左十右五之处。其画法为：以以上四点为圆心，各以一等分为半径，分别作四个圆。
'''
import turtle as t 
t.penup() 
t.goto(-330,220) 
t.pendown()
a = 1 
t.fillcolor('red') 
t.color('red') 
t.begin_fill() 
while a <= 4:
    if a % 2 == 1:
        t.fd(660) 
    else:
        t.fd(440) 
    t.rt(90) 
    a += 1 
t.end_fill()
#画五角星
t.penup() 
t.goto(-286,132)
b = 1 
t.fillcolor('yellow') 
t.color('yellow') 
t.begin_fill() 
while b <= 5:
    t.fd(132) 
    t.right(144) 
    b += 1 
t.end_fill()
t.penup() 
t.goto(-88,176) 
b = 1 
t.fillcolor('yellow') 
t.begin_fill() 
t.right(156) 
while b <= 5:
    t.fd(44)
    t.right(144)
    b += 1 
t.end_fill()
t.penup() 
t.goto(-88,132) 
b = 1 
t.fillcolor('yellow') 
t.begin_fill() 
t.right(180) 
while b <= 5:
    t.fd(44) 
    t.right(144) 
    b += 1 
t.end_fill()
t.penup() 
t.goto(-66,88)
b = 1 
t.fillcolor('yellow') 
t.begin_fill() 
t.right(90) 
while b <= 5:
    t.fd(44)
    t.right(144) 
    b += 1 
t.end_fill()
t.penup() 
t.goto(-88,22) 
b = 1 
t.fillcolor('yellow') 
t.begin_fill() 
t.right(90) 
while b <= 5:
    t.fd(44) 
    t.right(144)
    b += 1 
t.end_fill()
t.penup() 
t.goto(500,0) 
t.done()