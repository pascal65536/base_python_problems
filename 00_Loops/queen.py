import random


N = 0
M = 20
queen_x = random.randint(N, M)
queen_y = random.randint(N, M)
person_x = random.randint(N, M)
person_y = random.randint(N, M)
counter = 0
while True:
    dist = abs(person_x - queen_x) + abs(person_y - queen_y)
    print("X=", person_x, "Y=", person_y, "dist=", dist)
    if dist == 0:
        print("Победа!")
        print(f"Шагов: {counter}")
        break
    step = input("Ваш ход:")

    if not step:
        break
    if len(step) != 2:
        print("ОШИБКА 1")
        continue
    if step[0] not in "UDLR":
        print("ОШИБКА 2")
        continue
    if step[1] not in "0123456789":
        print("ОШИБКА 3")
        continue

    match step[0]:
        case "D":
            person_y -= int(step[1])
        case "U":
            person_y += int(step[1])
        case "L":
            person_x -= int(step[1])
        case "R":
            person_x += int(step[1])
    counter += 1
