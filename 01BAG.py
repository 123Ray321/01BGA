
#元素个数
num = 3
#价值
value = [60,80,100]
#重量
weight = [1,3,4]
#包的承重
bagSpace = 4

#行
item = []
#二维列表
mat = []

#初始化二维列表
for i in range(num):
    mat.append([])
for i in mat:
    for _ in range(bagSpace):
        i.append(0)

#暴力法
def Violence():
    allResult = []
    #列出所有结果,以二进制来代表选择了哪些商品
    for i in range(pow(2,num)):
        allResult.append(bin(i))

    #总重量
    totalWeight = 0
    #总价值
    totalValue = 0
    #最大价值
    maxValue = 0

    #判断列出的结果组合
    for row in allResult:
        judgeList = str(row)[2:].zfill(num)
        for j in range(num):
            # 判断商品的选取情况
            if judgeList[j] == '1':
                totalWeight += weight[j]
                totalValue += value[j]
        if totalWeight <= bagSpace:
            if totalValue > maxValue:
                maxValue = totalValue
        print("current:%s"%judgeList)
        print('total:',totalValue)
        print('maxValue:',maxValue)
        print('')
        totalValue = 0
        totalWeight = 0
    return maxValue

    # maxValue = 0
    #
    # #n选一
    # for i in range(num):
    #     if weight[i] <= bagSpace:
    #         if value[i] > maxValue:
    #             maxValue = value[i]
    # weightList = []
    # valueList = []
    #
    # #n选a(1<a<n)
    # #n选2
    # for i in range(num - 1):
    #     posSet.append(i)
    #     for j in range(i + 1,num):
    #         if weight[i] + weight[j] <= bagSpace:
    #             if value[i] + value[j] > maxValue:
    #                 maxValue = value[i] + value[j]
    #
    # sumW = 0
    # sumV = 0
    # #n选n
    # for i in range(num):
    #     sumW += weight[i]
    #     sumV += value[i]
    #
    # if sumW < bagSpace:
    #     if sumV > maxValue:
    #         maxValue = sumV
    # return maxValue

#动态规划法
def Dynamic(tMat):
    #遍历二维列表
    for i in range(num):
        for j in range(bagSpace):
            #第一行的处理
            if(i == 0):
                if(weight[i] <= (j + 1)):
                    tMat[i][j] = value[i]
                else:
                    tMat[i][j] = 0
            else:
                #其他行的处理
                if(weight[i] <= (j + 1)):
                    #处理当前物品装入之后，子背包还有剩余空间的情况
                    if((j + 1) - weight[i] > 0):
                        tMat[i][j] = value[i] + \
                                     tMat[i - 1][j - weight[i]]
                    else:
                        tMat[i][j] = value[i]
                else:
                    tMat[i][j] = tMat[i - 1][j]
                #将当前元素和上一行同列元素中较大的那一个赋给当前元素
                if(tMat[i - 1][j] > tMat[i][j]):
                    tMat[i][j] = tMat[i - 1][j]
    return tMat




violenceRes = Violence()
print('暴力法结果：')
print(violenceRes)
print('')

mat = Dynamic(mat)

#输出二维数组
for i in range(num):
    for j in range(bagSpace):
        print(mat[i][j],end = '   ')
    print("")
print('动态规划法结果：')
print(mat[num -1][bagSpace - 1])

