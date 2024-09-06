prg = """
move_right() 
move_right() 
move_right() 
move_down() 
for k in range(8): 
    move_up() 
move_left() 
for k in range(3): 
    move_left() 
move_down() 
for k in range(2): 
    move_down() 
move_right() 
# это последняя строка
"""

steps_dct = {
    "move_up": [1, 0],
    "move_down": [-1, 0],
    "move_right": [0, 1],
    "move_left": [0, -1],
}


def get_key(word):
    return int(word.split("(")[-1].split(")")[0])


mult = 1
maze_dct = dict()
for word in prg.split("\n"):
    if not word:
        continue
    if word == "# это последняя строка":
        continue
    word = word.replace("()", "(1)")


    if ":" in word:
        mult = get_key(word)
        continue
    elif word == word.lstrip():
        mult = 1
    
    maze_dct.setdefault(mult, list())
    maze = steps_dct.get(word.strip().split("(")[0].lower())
    steps = get_key(word)
    maze_dct[mult].append([maze[0] * steps, maze[1] * steps])

coords = [0, 0]
for mult, steps_lst in maze_dct.items():
    for stps in steps_lst:
        coords[0] += stps[0] * mult
        coords[1] += stps[1] * mult
        # for num in range(2):
        #     coords[num] += stps[num] * mult
print(coords)
