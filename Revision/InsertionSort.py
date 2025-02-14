def sort (arry):
    num = len(arry)

    if num <= 1:
        return
    
    for i in range (1, num):
        key = arry[i]
        x = i-1

        while x >= 0 and key < arry[x]:
            arry[x+1] = arry[x]
            x -= 1
        arry[x+1] = key

arry = [14,18,12,15,3,5]
sort(arry)
print(arry)