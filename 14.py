result_lst = list()
radix = 11
for x in "0123456789":
    first = "1800x6"
    second = "6x107"
    third = "1x63"
    first_new = first.replace("x", x)
    second_new = second.replace("x", x)
    third_new = third.replace("x", x)
    result = int(first_new, radix) + int(second_new, radix) - int(third_new, radix)
    if result % 7 == 0:
        result_lst.append(result // 7)
print(min(result_lst))