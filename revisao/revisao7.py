def invertString(s):
    revString = ""
    for x in s:
        revString = x + revString
    return revString

s = input('Insira o texto brother: ')
print(invertString(s))