fibb_lst = [0, 1]
while fibb_lst[-1] < 1000:
    fibb_lst.append(fibb_lst[-1] + fibb_lst[-2])
print(fibb_lst)
