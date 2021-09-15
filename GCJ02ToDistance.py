'''
顾名思义，这是一个计算两个GCJ02坐标系下点位间距离的方法
在这个下方这个函数中
getDistance(lat1, lng1, lat2, lng2)
lat1为第一个点的纬度，lng1为第一个点的经度
lat2和lng2同理
可以在这个网址进行校验
https://lbs.amap.com/demo/javascript-api/example/calcutation/calculate-distance-between-two-markers
'''

import math

def rad(d):
    return (d * math.pi / 180.0)


def getDistance(lat1, lng1, lat2, lng2):
    EARTH_RADIUS = 6378.137
    radLat1 = rad(lat1)
    radLat2 = rad(lat2)
    a = radLat1 - radLat2
    b = rad(lng1) - rad(lng2)

    dis = 2 * math.asin(math.sqrt(math.pow(math.sin(a / 2), 2) +
        math.cos(radLat1) * math.cos(radLat2) * math.pow(math.sin(b / 2), 2)))

    dis = dis * EARTH_RADIUS
    dis = '%.4f' % dis
    dis = float(dis) * 1000
    return (dis)

if __name__ == '__main__':
    a = getDistance(39.9024017, 116.2359759, 39.9023587, 116.2368279)
    print(a)

