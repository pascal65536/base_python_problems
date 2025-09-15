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


if __name__ == "__main__":
    ret = print_rectangle("0", 4, 6)
    print(ret)
