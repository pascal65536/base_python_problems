# start = int(input())
# stop = int(input())
# step = int(input())

# res = str()
# for i in range(start, stop + 1, step):
#     res += str(i)
#     res += ', '
# res = res.strip(' ,')
# print(res)

word = input()
for num, ch in enumerate(word):
    res = ''
    for i in range(num + 1):
        res += f'{ch}-'
    res = res.strip('-')
    if num < len(word) - 1:
        res += ';'
    else:
        res += '.'
    print(res)
