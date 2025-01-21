# ----------Implemente o algoritmo Merge Sort sem utilizar funções ou bibliotecas prontas.-----------

def sort (arry):
    if len(arry) > 1:
        left = arry[:len(arry)//2]
        right = arry[len(arry)//2:]

        sort = left
        sort = right

        x = 0
        y = 0
        z = 0
        while x < len(left) and y < len(right):
            if left[x] < right[y]:
                arry[z] = left[x]
                x += 1
                z += 1
            else:
                arry[z] = right[y]
                x += 1
                z += 1
        
        while x < len(left):
            arry[z] = left[x]
            x += 1
            z += 1
        while z < len(right):
            arry[z] = right[x]
            y += 1
            z += 1

    return arry

arry = [12,2,6,8,14,8]

test = sort(arry)
print(test)