maxWight =eval(input("输入背包容量"))
weight = eval(input("依次输入商品重量"))
value = eval(input("依次输入商品价格"))
arr = [(i, value[i]/weight[i], weight[i], value[i])
       for i in range(len(weight))]


arr.sort(key=lambda x: x[1], reverse=True)
bagVal = 0
bagList = []
costList = []
for i, per, weight, value in arr:
    if weight <= maxWight:
        maxWight -= weight
        bagVal += value
        bagList.append(i)
        costList.append(weight)
    else:
        bagVal += maxWight*per
        bagList.append(i)
        costList.append(maxWight)
        break


print('\n排序后：', arr)
print('能运走的最大价值：%.2f' % bagVal)
print('此时承载的宝物有：', bagList)
print('货物依次取出：', costList)
