def checkNum(num, list):
    x = 0
    for i in range(0, len(list)):
        if num == list[i]:
            x += 1
    if x == 0:
        return True
    else:
        return False


def checkList(list):
    resList = []
    for i in range(0, len(list)):
        if checkNum(list[i], resList):
            resList.append(list[i])
    return resList


numlist = [1, 1, 11, 6, 6, 7, 3, 12, 13, 12, 22, 3, 4, 5, 13, 6, 7]
reslist = checkList(numlist)
print(reslist)
