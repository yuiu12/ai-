'''
输入车的数量，使用input函数
输出最小时间及车辆，需要使用判断大小的方法
需要判断输入的时间是否符合时间格式，不符合则重新输入
可以考虑使用def创建函数
'''
def CarRace(m):
    min = 10000 
    time = min1 = 0 
    c = 1 
    while c <= m:
        #提供的函数对指定序列做映射
        begin, end = map(int,input(f'请输入第{c}量车出发及结束时间(中间用空格隔开):').split())
        '''
        0 <= begin // 100 <= 23: 检查begin的整数部分是否在0到23之间，即检查小时是否在有效的范围内。
        0 <= end // 100 <= 23: 检查end的整数部分是否也在0到23之间，确保结束时间同样在一天的有效小时范围内。
        0 <= begin % 100 <= 59: 检查begin的分钟部分是否在0到59之间，确保开始时间的分钟数是有效的。
        0 <= end % 100 <= 59: 检查end的分钟部分是否也在0到59之间，确保结束时间的分钟数也是有效的。
        '''
        if 0 <= begin // 100 <= 23 and 0 <= end // 100 <= 23 and 0 <= begin % 100 <= 59 and 0 <= end % 100 <= 59:
            if end % 100 - begin % 100 >= 0:
                time = end - begin 
            else:
                time = end - begin - 40 
            if time <= min and end // 100 < 16:
                min = time 
                min1 = c 
            c += 1 
        else:
            print(f'您输入的第{c}量车时间不正确，请重新输入')
    if min1 != 0:
        print(f'第{min1}量车用时最短',end=', ')
        print(f'其用时为{min}，即{(min - min % 100) / 100}时{min % 100}分')
    else:print(-1)
m = int(input('请输入车的数量:')) 
CarRace(m)