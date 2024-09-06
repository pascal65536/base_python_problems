def print_rectangle(fill_char, height, width):
    if len(fill_char) != 1:
        return "Заполнитель должен быть длиной 1 символ"
    if height < 1:
        return "Высота должна быть больше 0"
    if width < 1:
        return "Ширина должна быть больше 0"
    for i in range(0, height):
        print(fill_char * width)
    return "Ok"


# ------------------------------------------------------------------
ret = print_rectangle("0", 2, 90)
print(ret)
