def bubble(arry):
    for j in range(len(arry) - 1):
        for i in range(len(arry) - 1):
            if arry[i] > arry[i+1]:
                arry[i], arry[i+1] = arry[i+1], arry[i]
    return arry

ulist = [4,3,6,7,8,1,9,2]
bubble(ulist)
print(ulist)