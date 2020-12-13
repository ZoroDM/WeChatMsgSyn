import math
import sys

# 客户兑换总积分
totalPoint = int(sys.stdin.readline())
# 计算值和预期值的差值，初始化默认为totalPoint
gap = totalPoint
# 上浮、下浮的范围
downFloatRange = 0
upFloatRange = 0.03
maxCount = 5

# 预期值的范围
downTotalPoint = totalPoint * (1 - downFloatRange)
upTotalPoint = totalPoint * (1 + upFloatRange)

productPrice = [17500, 27500, 37500, 47500, 70000, 84000, 90000, 140000, 420000, 560000, 700000, 2000000]
productName = ['洗护一', '洗护二', '洗护三', '洗护四', '日常保洁', '家电', '玻璃', '厨房/卫生间、深25平、地板打蜡、除螨卧室', '深一居室', '深二居室', '深三居室', '甲醛']
productMaxCount = []
for i in productPrice:
    temp = math.floor(upTotalPoint / i) if maxCount > math.floor(upTotalPoint / i) else maxCount
    productMaxCount.append(temp+1)

print(productMaxCount)

break_flag = False
for a11 in range(0, productMaxCount[11]):
    for a10 in range(0, productMaxCount[10]):
        for a9 in range(0, productMaxCount[9]):
            for a8 in range(0, productMaxCount[8]):
                for a7 in range(0, productMaxCount[7]):
                    for a6 in range(0, productMaxCount[6]):
                        for a5 in range(0, productMaxCount[5]):
                            for a4 in range(0, productMaxCount[4]):
                                for a3 in range(0, productMaxCount[3]):
                                    for a2 in range(0, productMaxCount[2]):
                                        for a1 in range(0, productMaxCount[1]):
                                            for a0 in range(0, productMaxCount[0]):
                                                a = [a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11]
                                                result = 0
                                                for j in range(0, 11):
                                                    result = result + a[j] * productPrice[j]
                                                interval = result - totalPoint
                                                if downTotalPoint <= result <= upTotalPoint:
                                                    if result == totalPoint:
                                                        print('差值为：0')
                                                        print(a)
                                                        break_flag = True
                                                    else:
                                                        if interval < gap:
                                                            gap = interval
                                                            print('差值为：', end="")
                                                            print(interval)
                                                            print(a)
                                            if break_flag:
                                                break
                                        if break_flag:
                                            break
                                    if break_flag:
                                        break
                                if break_flag:
                                    break
                            if break_flag:
                                break
                        if break_flag:
                            break
                    if break_flag:
                        break
                if break_flag:
                    break
            if break_flag:
                break
        if break_flag:
            break
    if break_flag:
        break

print('end')
