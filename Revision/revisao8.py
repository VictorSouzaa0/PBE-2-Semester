ob = []
dc = {}
def count_char(s):
    for i in s:
        ob.append(i)
        for x in ob:
            dc[x] = ob.count(x)
    return dc
s = input('Insira uma fruta: ')
print(count_char(s))