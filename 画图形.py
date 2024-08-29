'''
按照要求使用turtle库画出图形
画半径为50的圆；
画长方形；
画边长为100的红色五角星
'''
# import turtle 
# turtle.circle(50) 
# turtle.done()
'''
turtle.circle()函数
语法：
turtle.circle(radius, extent=None, steps=None)
参数说明：
radius(半径)：半径为正(负)，表示圆心在画笔的左边(右边)画圆；
extent(弧度) (optional)；
steps (optional) (做半径为radius的圆的内切正多边形，多边形边数为steps)。
'''

#画长方形
# import turtle
# i = 1
# while i <= 4:
#     if i % 2 == 1:
#         turtle.fd(100)
#     else:
#         turtle.fd(50)
#     turtle.left(90)
#     i += 1
# turtle.done()


#画边长为100的红色五角星
# import turtle 
# i = 1 
# turtle.fillcolor('red') 
# turtle.color('red') 
# turtle.begin_fill() 
# while i <= 5:
#     turtle.fd(100) 
#     turtle.right(144) 
#     i += 1 
# turtle.end_fill() 
# turtle.done()

#全部放在一起
import turtle 
#画半径为50的圆
turtle.circle(50) 
#画长方形
#抬起画笔
turtle.penup() 
#移动画笔到坐标 (-100, 0)
turtle.goto(-100,0) 
turtle.right(180) 
#放下画笔开始绘制图形
turtle.pendown() 
i = 1 
while i <= 4:
    if i % 2 == 1:
        turtle.fd(100)
    else:
        turtle.fd(50) 
    turtle.left(90) 
    i += 1 
turtle.left(180)
#画边长为100的红色五角星
turtle.penup() 
turtle.goto(100,0) 
turtle.pendown() 
i = 1 
turtle.fillcolor('red')
turtle.color('red') 
turtle.begin_fill() 
while i <= 5:
    turtle.fd(100) 
    turtle.right(144) 
    i += 1 
turtle.end_fill() 
turtle.done()